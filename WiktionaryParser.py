import collections
import re
import bz2

from lxml import etree

import wikitextparser
import wiktlangs
from wikiutils import *
import definitions # LF: local file


def parseEtymology(word, data, text):
    """From the etymology section we parse "compound", "affix", and
    "suffix" templates.  These may suggest that the word is a compound
    word.  They are stored under "compound"."""

    wordEtymology = wikitextparser.parse(text)

    for t in wordEtymology.templates:
        name = t.name.strip()
        if name in etymologyShortcuts:
            name = etymologyShortcuts[name]
        if name in etymologyTemplates:
            # XXX LF rn affixes into pre- and suffixes? 
            if name in argsMap:
                ht = {}
                for x in t.arguments:
                    arg = x.name.strip()
                    if arg in argsMap[name]:
                        arg = argsMap[name][arg]
                    value = x.value
                    ht[arg] = clean_value(value)
                ht["relationship"] = name
                data_append(data, "etymology", ht)
            else:
                data_append(data, "etymology", template_args_to_dict(t))


class WiktionaryParser(object):
    """This class is used for XML parsing the Wiktionary dump file."""

    def __init__(self, word_cb, capture_cb,
                 capture_languages, capture_translations,
                 capture_pronunciation, capture_linkages,
                 capture_compounds, capture_redirects):
        assert callable(word_cb)
        assert capture_cb is None or callable(capture_cb)
        assert isinstance(capture_languages, (list, tuple, set))
        for x in capture_languages:
            assert isinstance(x, str)
        assert capture_translations in (True, False)
        assert capture_linkages in (True, False)
        assert capture_translations in (True, False)
        self.word_cb = word_cb
        self.capture_cb = capture_cb
        self.capture_languages = capture_languages
        self.capture_translations = capture_translations
        self.capture_pronunciation = capture_pronunciation
        self.capture_linkages = capture_linkages
        self.capture_compounds = capture_compounds
        self.capture_redirects = capture_redirects
        self.tag = None
        self.namespaces = {}
        self.stack = []
        self.text = None
        self.title = None
        self.pageid = None
        self.redirect = None
        self.model = None
        self.format = None
        self.language_counts = collections.defaultdict(int)
        self.pos_counts = collections.defaultdict(int)
        self.section_counts = collections.defaultdict(int)


    def start(self, tag, attrs):
        """This is called whenever an XML start tag is encountered."""
        idx = tag.find("}")
        if idx >= 0:
            tag = tag[idx + 1:]
        attrs = {re.sub(r".*}", "", k): v for k, v in attrs.items()}
        tag = tag.lower()
        #while tag in self.stack:
        #    self.end(self.stack[-1])
        self.tag = tag
        self.stack.append(tag)
        self.attrs = attrs
        self.data = []
        if tag == "page":
            self.text = None
            self.title = None
            self.pageid = None
            self.redirect = None
            self.model = None
            self.format = None

    def end(self, tag):
        """This function is called whenever an XML end tag is encountered."""
        idx = tag.find("}")
        if idx >= 0:
            tag = tag[idx + 1:]
        tag = tag.lower()
        ptag = self.stack.pop()
        assert tag == ptag
        attrs = self.attrs
        data = "".join(self.data).strip()
        self.data = []
        if tag in definitions.ignore_tags:
            return
        for t in definitions.stack_ignore:
            if t in self.stack:
                return
        if tag == "id":
            if "revision" in self.stack:
                return
            self.pageid = data
        elif tag == "title":
            self.title = data
        elif tag == "text":
            self.text = data
        elif tag == "redirect":
            self.redirect = attrs.get("title")
        elif tag == "namespace":
            key = attrs.get("key")
            self.namespaces[key] = data
        elif tag == "model":
            self.model = data
            if data not in ("wikitext", "Scribunto", "css", "javascript",
                            "sanitized-css"):
                print("UNRECOGNIZED MODEL", data)
        elif tag == "format":
            self.format = data
            if data not in ("text/x-wiki", "text/plain",
                            "text/css", "text/javascript"):
                print("UNRECOGNIZED FORMAT", data)
        elif tag == "page":
            pageid = self.pageid
            title = self.title
            redirect = self.redirect
            if self.model in ("css", "sanitized-css", "javascript",
                              "Scribunto"):
                return
            if redirect:
                if self.capture_redirects:
                    data = {"redirect": redirect, "word": title}
                    self.word_cb(data)
            else:
                # If a capture callback has been provided, skip this page.
                if self.capture_cb and not self.capture_cb(title, self.text):
                    return
                # Parse the page, and call ``word_cb`` for each captured
                # word.
                ret = parsePage(title, self.text, self)
                for data in ret:
                    self.word_cb(data)
        else:
            print("UNSUPPORTED", tag, len(data), attrs)

    def data(self, data):
        """This function is called for data within an XML tag."""
        self.data.append(data)

    def close(self):
        """This function is called when parsing is complete."""
        return None

def pageIterator(word, text, ctx):
    """Iterates over the text of the page, returning words (parts-of-speech)
    defined on the page one at a time.  (Individual word senses for the
    same part-of-speech are typically encoded in the same entry.)"""
    assert isinstance(word, str)
    assert isinstance(text, str)
    assert isinstance(ctx, WiktionaryParser)

    # Divide the text into subsections.  We ignore the tree structure of
    # sections because it has so many inconsistencies.
    sections = split_subsections(text)

    def iteratorFunction():
        language = None
        pos = None
        base = {}
        words = []
        wordData = {}

        def flushPos():
            # Flushes information about the current part-of-speech entry.
            nonlocal wordData
            if language in ctx.capture_languages and pos is not None:
                wordData["pos"] = pos
                words.append(wordData)
                wordData = {}

        def flushWord():
            # Flushes information about the current part-of-speech entry.
            nonlocal wordData
            if language in ctx.capture_languages:
                wordData["pos"] = pos
                words.append(wordData)
                wordData = {}

        def flushWords():
            # Returns datas for parts-of-speech for the current language,
            # merging information from the base (for all entries) with
            # information for each specific entry.
            ret = []
            for w in words:
                # XXX this merging needs more work
                dt = base.copy()
                for k, v in w.items():
                    if k in dt and k not in ("sounds",):
                        dt[k] = dt[k] + v
                    else:
                        dt[k] = v
                ret.append(dt)
            return ret

        # Iterate over all sections on the page, looking for sections whose
        # name matches the name of a known language.
        for sectitle, text in sections:
            if sectitle in wiktlangs.languages:
                # Found section for a langauge.  First flush any information
                # for the previous language.
                # flushPos()
                flushWord()
                flushWords()
                for w in flushWords():
                    yield w

                # Initialize for parsing words in the new language.
                language = sectitle
                ctx.language_counts[language] += 1
                pos = None
                base = {"word": clean_value(word), "lang": language}
                wordData = {}
                words = []
                sectitle = ""
            else:
                # This title continues the previous language or could be
                # a new language or a misspelling or a previously unsupported
                # subtitle.
                sectitle = sectitle.lower()
                # if sectitle in pos_map:
                #     # New part-of-speech.  Flush the old part-of-speech.
                #     flushPos()
                #     # Initialize for parsing the new part-of-speech.
                #     pos = pos_map[sectitle]
                #     ctx.pos_counts[pos] += 1
                #     wordData = {}
                #     sectitle = ""
                # else:
                #     # We don't recognize this subtitle.  Include it in the
                #     # counts; the counts should be periodically investigates
                #     # to find out if new languages have been added.
                ctx.section_counts[sectitle] += 1

            # Check if this is a language we are capturing.  If not, just
            # skip the section.
            if language not in ctx.capture_languages:
                continue

            # LF: Commented out because it was removing Etymology 1 sections
            # if pos is None:
            #     # Have not yet seen a part-of-speech.  However, this initial
            #     # part frequently contains pronunciation information that
            #     # is shared by all parts of speech.  We don't care here
            #     # whether it is under a ``pronunciation`` subsection, because
            #     # the structure may vary.
            #     if ctx.capture_pronunciation:
            #         p = wikitextparser.parse(text)
            #         parse_pronunciation(word, base, text, p)
            #     continue

            # Remove any numbers at the end of the section title.
            sectitle = re.sub(r"\s+\d+(\.\d+)$", "", sectitle)

            # Apply corrections to common misspellings in sectitle
            if sectitle in sectitle_corrections:
                sectitle = sectitle_corrections[sectitle]

            # Mostly ignore etymology sections, as they often seem to contain
            # links that could be misinterpreted as something else.
            # We don't want to completely ignore Usage notes or References
            # or Anagrams, as they are often the last section of an entry
            # and thus completely ignoring them might miss classifications
            # etc.
            #
            # However, we do want to collect information about the parts of
            # compound words from the etymology sections (this is particularly
            # useful for Finnish).
            if sectitle.startswith("etymology"):
                parseEtymology(word, wordData, text)
                continue

            # # Parse the section contents.
            # p = wikitextparser.parse(text)

            # # If the section title is empty, it is the preamble (text before
            # # the first subsection for the language).
            # if sectitle == "":  # Preamble
            #     parse_preamble(word, wordData, pos, text, p)
            # # If the section title title indicates pronunciation, parse it here.
            # elif sectitle == "pronunciation":
            #     if ctx.capture_pronunciation:
            #         parse_pronunciation(word, wordData, text, p)
            # # Parse various linkage sections, defaulting to the linkage type
            # # indicated by the section header.
            # elif sectitle == "synonyms":
            #     if ctx.capture_linkages:
            #         parse_linkage(word, wordData, "synonyms", text, p)
            # elif sectitle == "hypernyms":
            #     if ctx.capture_linkages:
            #         parse_linkage(word, wordData, "hypernyms", text, p)
            # elif sectitle == "hyponyms":
            #     if ctx.capture_linkages:
            #         parse_linkage(word, wordData, "hyponyms", text, p)
            # elif sectitle == "antonyms":
            #     if ctx.capture_linkages:
            #         parse_linkage(word, wordData, "antonyms", text, p)
            # elif sectitle == "derived terms":
            #     if ctx.capture_linkages:
            #         parse_linkage(word, wordData, "derived", text, p)
            # elif sectitle == "related terms":
            #     if ctx.capture_linkages:
            #         parse_linkage(word, wordData, "related", text, p)
            # # Parse abbreviations.
            # elif sectitle == "abbreviations":
            #     parse_linkage(word, wordData, "abbreviations", text, p)
            # # Parse proverbs.
            # elif sectitle == "proverbs":
            #     parse_linkage(word, wordData, "abbreviations", text, p)
            # # Parse compounds using the word.
            # elif sectitle == "compounds":
            #     if ctx.capture_compounds:
            #         parse_linkage(word, wordData, "compounds", text, p)
            # # We skip declension information here, as it is parsed from all
            # # sections in parse_any().
            # elif sectitle in ("declension", "conjugation"):
            #     pass
            # # XXX warn on other sections

            # # XXX LF: parse etymology function?
            
            # # Some information is parsed from any section.
            # parse_any(word, base, wordData, text, pos, sectitle,
            #           p, ctx.capture_translations)

        # Finally flush the last language.
        flushPos()
        for w in flushWords():
            yield w

    return iteratorFunction()

def parsePage(word, text, ctx):
    """Parses the text of a Wiktionary page and returns a list of dictionaries,
    one for each word/part-of-speech defined on the page for the languages
    specified by ``capture_languages``.  ``word`` is page title, and ``text``
    is page text in Wikimedia format.  Other arguments indicate what is
    captured."""
    assert isinstance(word, str)
    assert isinstance(text, str)
    assert isinstance(ctx, WiktionaryParser)

    # Collect all words from the page.
    words = list(x for x in pageIterator(word, text, ctx))

    # # Do some post-processing on the words.  For example, we may distribute
    # # conjugation information to all the words.
    # for wordIterator in words:
    #     # If one of the words coming from this article does not have
    #     # conjugation information, but another one has, use the information
    #     # from the other one also for the one without.
    #     if "conjugation" not in wordIterator:
    #         pos = wordIterator.get("pos")
    #         assert pos
    #         for dt in words:
    #             conjs = dt.get("conjugation", ())
    #             if not conjs:
    #                 continue
    #             cpos = dt.get("pos")
    #             if (pos == cpos or
    #                 (pos, cpos) in (("noun", "adj"),
    #                                 ("noun", "name"),
    #                                 ("name", "noun"),
    #                                 ("name", "adj"),
    #                                 ("adj", "noun"),
    #                                 ("adj", "name")) or
    #                 (pos == "adj" and cpos == "verb" and
    #                  any("participle" in s.get("tags", ())
    #                      for s in dt.get("senses", ())))):
    #                 wordIterator["conjugation"] = conjs
    #                 break

    # XXX some other information is global to page, e.g., the Category links.
    # such information should be distributed to all words on the page
    # (or perhaps all nouns, or perhaps only Enligh nouns?).

    # Return the resulting words
    return words

def parseWiktionary(path, word_cb, capture_cb=None,
                     languages=["English", "Translingual"],
                     translations=False,
                     pronunciations=False,
                     linkages=False,
                     compounds=False,
                     redirects=False):
    """Parses Wiktionary from the dump file ``path`` (which should point
    to a "enwiktionary-<date>-pages-articles.xml.bz2" file.  This
    calls ``capture_cb(title)`` for each raw page (if provided), and
    if it returns True, and calls ``word_cb(data)`` for all words
    defined for languages in ``languages``.  The other keyword
    arguments control what data is to be extracted."""
    assert isinstance(path, str)
    assert callable(word_cb)
    assert capture_cb is None or callable(capture_cb)
    assert isinstance(languages, (list, tuple, set))
    for x in languages:
        assert isinstance(x, str)
        assert x in wiktlangs.languages
    assert translations in (True, False)
    assert pronunciations in (True, False)
    assert linkages in (True, False)
    assert compounds in (True, False)
    assert redirects in (True, False)

    # Open the input file.
    if path.endswith(".bz2"):
        wikt_f = bz2.BZ2File(path, "r", buffering=(4 * 1024 * 1024))
    else:
        wikt_f = open(path, "rb", buffering=(4 * 1024 * 1024))

    try:
        # Create parsing context.
        ctx = WiktionaryParser(word_cb, capture_cb,
                               languages, translations,
                               pronunciations, linkages, compounds,
                               redirects)
        # Parse the XML file.
        parser = etree.XMLParser(target=ctx)
        etree.parse(wikt_f, parser)
    finally:
        wikt_f.close()

    # Return the parsing context.  At least the statistics fields are
    # accessible:
    #   ctx.language_counts
    #   ctx.pos_counts
    #   ctx.section_counts
    return ctx
