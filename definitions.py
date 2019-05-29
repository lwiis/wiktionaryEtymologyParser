import re

# These XML tags are ignored when parsing.
ignore_tags = set(["sha1", "comment", "username", "timestamp",
                   "sitename", "dbname", "base", "generator", "case",
                   "ns", "restrictions", "contributor", "username",
                   "minor", "parentid", "namespaces", "revision",
                   "siteinfo", "mediawiki",
])

# Other tags are ignored inside these tags.
stack_ignore = ["contributor"]

# These Wiktionary templates are silently ignored (though some of them may be
# used when cleaning up titles and values).
ignored_templates = set([
    "-",
    "=",
    "*",
    "!",
    ",",
    "...",
    "AD",
    "BCE",
    "B.C.E.",
    "Book-B",
    "C.",
    "CE",
    "C.E.",
    "BC",
    "B.C.",
    "A.D.",
    "Clade",  # XXX Might want to dig information from this for hypernyms
    "CURRENTYEAR",
    "EtymOnLine",
    "EtymOnline",
    "IPAchar",
    "LR",
    "PAGENAME",
    "Q",
    "Webster 1913",
    "\\",
    "abbreviation-old",
    "af",
    "affix",
    "altcaps",
    "anchor",
    "ante",
    "attention",
    "attn",
    "bor",
    "borrowed",
    "bottom",
    "bottom2",
    "bottom3",
    "bottom4",
    "bullet",
    "checksense",
    "circa",
    "circa2",
    "cite",
    "cite book",
    "Cite news",
    "cite news",
    "cite-book",
    "cite-journal",
    "cite-magazine",
    "cite-news",
    "cite-newgroup",
    "cite-song",
    "cite-text",
    "cite-video",
    "cite-web",
    "cite web",
    "cog",
    "col-top",
    "col-bottom",
    "datedef",
    "def-date",
    "defdate",
    "defdt",
    "defn",
    "der",
    "der-bottom",
    "der-bottom2",
    "der-bottom3",
    "der-bottom4",
    "der-mid2",
    "der-mid3",
    "der-mid4",
    "der-mid",
    "derived",
    "dot",
    "doublet",
    "eggcorn of",
    "ellipsis",
    "em dash",
    "en dash",
    "etyl",
    "example needed",
    "examples",
    "examples-right",
    "frac",
    "g",  # gender - too rare to be useful
    "gloss-stub",
    "glossary",
    "hyp2",
    "hyp-top",
    "hyp-mid",
    "hyp-mid3",
    "hyp-bottom3",
    "hyp-bottom",
    "inh",
    "inherited",
    "interwiktionary",
    "ISO 639",
    "jump",
    "katharevousa",
    "ko-inline",
    "lang",
    "list",
    "ll",
    "lookfrom",
    "m",
    "mention",
    "mid2",
    "mid3",
    "mid4",
    "mid4",
    "middot",
    "multiple images",
    "nb...",
    "nbsp",
    "ndash",
    "no entry",
    "noncog",
    "noncognate",
    "nowrap",
    "nuclide",
    "overline",
    "phrasebook",
    "pedia",
    "pedialite",
    "picdic",
    "picdiclabel",
    "picdiclabel/new",
    "pos_v",
    "post",
    "quote-book",
    "quote-journal",
    "quote-magazine",
    "quote-news",
    "quote-newsgroup",
    "quote-song",
    "quote-text",
    "quote-video",
    "quote-web",
    "redirect",
    "rel-bottom",
    "rel-mid",
    "rel-mid2",
    "rel-mid3",
    "rel-mid4",
    "rfap",
    "rfc",
    "rfc-auto",
    "rfc-def",
    "rfc-header",
    "rfc-level",
    "rfc-subst",
    "rfc-tsort",
    "rfc-sense",
    "rfcite-sense",
    "rfd-redundant",
    "rfd-sense",
    "rfdate",
    "rfdatek",
    "rfdef",
    "rfe",
    "rfex",
    "rfexample",
    "rfm-sense",
    "rfgloss",
    "rfquote",
    "rfquote-sense",
    "rfquotek",
    "rft-sense",
    "rfv-sense",
    "rhymes",
    "rhymes",
    "see",
    "see also",
    "seeCites",
    "seemoreCites",
    "seemorecites",
    "seeMoreCites",
    "seeSynonyms",
    "sic",
    "smallcaps",
    "soplink",
    "spndash",
    "stroke order",
    "stub-gloss",
    "sub",
    "suffixsee",
    "sup",
    "syndiff",
    "t-check",
    "t+check",
    "table:colors/fi",
    "top2",
    "top3",
    "top4",
    "translation only",
    "trans-mid",
    "trans-bottom",
    "uncertain",
    "unk",
    "unsupported",
    "used in phrasal verbs",
    "was wotd",
    "wikisource1911Enc",
    "wikivoyage",
    "ws",
    "ws link",
    "zh-hg",
])

# LF: XXX move to constants at top so it's only declared once
# LF: XXX build a substitution map for shortcut forms of templates
etymologyTemplates = set([
    "derived",
    "der",
    "borrowed",
    "bor",
    "learned borrowing",
    "lbor",
    "orthographic borrowing",
    "obor",
    "inherited",
    "inh",
    "PIE root",
    "affix",
    "prefix",
    "confix",
    "suffix",
    "compound"
    "blend",
    "clipping",
    "short for",
    "back-form",
    "doublet",
    "onomatopoeic",
    "onom",
    "calque",
    "semantic loan",
    "named-after",
    "phono-semantic matching",
    "psm",
    "mention",
    "m",
    "cognate",
    "cog",
    "noncognate",
    "noncog",
    "langname-mention",
    "m+"
])

etymologyShortcuts = {
    "der": "derived",
    "bor": "borrowed",
    "lbor":  "learned borrowing",
    "obor": "orthographic borrowing",
    "inh": "inherited",
    "onom": "onomatopoeic",
    "psm": "phono-semantic matching",
    "m": "mention",
    "cog": "cognate",
    "noncog": "noncognate",
    "langname-mention": "mention",
    "m+": "mention"
}

borrowedArgsMap = {
    # When to use
    # This template is intended specifically for loanwords that were borrowed 
    # during the time the borrowing language was spoken 

    # Parameters
    # |1= The language code (see Wiktionary:Languages) of the language which borrowed the term
    # |2= The language code of the source language from which the term was borrowed.
    # |3= The term in the source language that this term was borrowed from. 
    # |4= or |alt= (optional) An alternative display form to show for the term, see {{l}} and {{m}}.
    # |5= or |t= or |gloss= (optional) A gloss/translation for the term, see {{l}} and {{m}}.
    # |tr= (optional) A transliteration for the term, see {{l}} and {{m}}.
    # |pos= (optional) A part of speech indication for the term, see {{l}} and {{m}}.
    # |g=, |g2=, |g3= and so on(optional) Gender and number, as in {{l}} and {{m}}; 
    # |lit= (optional) A literal translation for the term, see {{l}} and {{m}}.
    # |id= (optional) A sense id for the term, see {{l}} and {{m}}.
    # |sc= (optional) Script code to use, see {{l}} and {{m}}.
    # |sort= (optional) Sort key. Not normally needed.

    '1': "language",
    '2': "source language",
    '3': "source word",
    '4': "alt",
    "alt": "alt",
    '5': "gloss",
    "t": "gloss",
    "gloss": "gloss",
    "pos": "pos",
    "tr": "transliteration",
    "g": "gender/number", # XXX what about other gs?
    "lit": "translation",
    "id": "id",
    "sc": "script code"
}

mentionArgsMap = {
    # When to use
    # This template generates a link to an entry in a given language. 
    # It links to a specific language-section on the target page, and applies language-specific 
    # formatting. It can also show a number of annotations after the linked term.

    # Parameters
    # |1= The language code (see Wiktionary:Languages) for the language that the term is in. 
    # |2= (optional) The page name to be linked to. 
    # |3= (optional) Alternate text to display as the link title, if different from the page name. 
    # |t= or |4= (optional) A gloss or short translation of the word. 
    # |sc= (optional) The script code (see Wiktionary:Scripts) for the script that the term is written in. 
    # |tr= (optional) Transliteration for non-Latin-script words. 
    # |ts= (optional) Transcription for non-Latin-script words whose transliteration is markedly different from the actual pronunciation. 
    # |pos= (optional) A part of speech indication for the term.
    # |g=, |g2=, |g3= and so on (optional) Gender and number; see Module:gender and number for details.
    # |lit= (optional) A literal translation for the term.
    # |id= (optional) A sense id for the term, which links to anchors on the page set by the {{senseid}} template.

    '1': "language",
    '2': "word",
    '3': "alt word",
    'alt': "alt word",
    'title': "title", # for onomatopoeias
    '4': "gloss",
    "t": "gloss",
    "pos": "pos",
    "tr": "transliteration",
    "ts": "transcriptions",
    "g": "gender/number", # XXX what about other gs?
    "lit": "translation",
    "id": "id",
    "sc": "script code"
}

affixArgsMap = {
    # When to use
    # This template shows the parts (morphemes) that make up a word.

    # Parameters
    # |1= The language code (see Wiktionary:Languages) for the language that the term is in. 
    # |sc= (optional) The script code (see Wiktionary:Scripts) for the script that the term is written in. 
    # |2=, |3= etc. parts of the words to show. Either: 1) At least one of the provided parts must begin and/or end with a hyphen (prefix, suffix, interfix); 2) or there must be two or more parts (it may be a compound, with or without prefixes, suffixes, interfixes).
    # |pos= The part of speech to include in the category names, in plural form. Defaults to words.
    # The following parameters are available for each matching part in the numbered/positional parameters. The N must be replaced by the corresponding part index. For example, for the second part (positional parameter 3), use 2 for N. Most of these parameters correspond directly to the equivalent parameters in the standard {{l}} (and {{m}}) template.
    # |altN= The alternative display form. Equivalent to the third parameter of {{l}}.
    # |tN= A gloss to show after the part. Equivalent to the fourth parameter of {{l}}. The parameter |glossN= is deprecated for this purpose.
    # |trN= The transliteration, as in {{l}}.
    # |tsN= The transcription, in languages where the transliteration and transcription differ markedly, as in {{l}}.
    # |gN= The gender (multiple comma-separated genders may be specified for a given part).
    # |idN= The sense id, as in {{l}}. As distinguished by mere linking templates, the affix template, categorizing terms by affix, also adds the sense id to the category name to distinguish various purposes of the same affix shape, hence the sense id in the dictionary entry for the affix should have a reasonable name in respect to this categorization. Changes the category name from language name terms affixed with affix to language name terms affixed with affix (value of id parameter).
    # |posN= The part of speech label to show after the part, as in {{l}}. If this parameter contains patronym(ic), the entry will be added to a language's patronymic category. If this parameter contains diminutive and the |pos= parameter is defined, the entry will be added to a diminutive part-of-speech category. For instance, the parameter values |pos=noun and |pos2=diminutive suffix will add an entry to the language's diminutive nouns category.
    # |litN= The literal meaning to show after the part, as in {{l}}.
    # |qN= Qualifier text to display after the part, in parens and normally italicized.
    # |langN= language code to use for this particular part. This overrides the default provided by |1=. When this is provided, the language name is displayed before the part, and a derivational category is also added to the entry. This is used for the occasional term which was directly affixed at the time of borrowing, and for which no native base form existed at the time, such as vexillology.
    # |scN= The script code to use for this particular part. This overrides the default provided by |sc=.

    '1': "language",
    "sc": "script code",
    '2': "word 1",
    '3': "word 2",
    '4': "word 3",
    '5': "word 4",
    "pos": "pos",
    "alt1": "alt 1",
    "alt2": "alt 2",
    "alt3": "alt 3",
    "alt4": "alt 4",
    "t1": "gloss 1",
    "t2": "gloss 2",
    "t3": "gloss 3",
    "t4": "gloss 4",
    "tr1": "transliteration 1",
    "tr2": "transliteration 2",
    "tr3": "transliteration 3",
    "tr4": "transliteration 4",
    "ts1": "transcription 1",
    "ts2": "transcription 2",
    "ts3": "transcription 3",
    "ts4": "transcription 4",
    "g1": "gender/number 1", # XXX what about other gs?
    "g2": "gender/number 2", # XXX what about other gs?
    "g3": "gender/number 3", # XXX what about other gs?
    "g4": "gender/number 4", # XXX what about other gs?
    "id1": "id 1",
    "id2": "id 2",
    "id3": "id 3",
    "id4": "id 4",
    "pos1": "pos 1",
    "pos2": "pos 2",
    "pos3": "pos 3",
    "pos4": "pos 4",
    "lit1": "translation 1",
    "lit2": "translation 2",
    "lit3": "translation 3",
    "lit4": "translation 4",
    "q1": "qualifier 1",
    "q2": "qualifier 2",
    "q3": "qualifier 3",
    "q4": "qualifier 4",
    "lang1": "language 1",
    "lang2": "language 2",
    "lang3": "language 3",
    "lang4": "language 4",
    "sc1": "script 1",
    "sc2": "script 2",
    "sc3": "script 3",
    "sc4": "script 4"
}

prefixArgsMap = {
    # When to use
    # This template is used in the etymology section. Use {{prefix|language code|prefix|root}}
    # where prefix is the prefix, excluding hyphen, and root is the root of the term.

    # Parameters
    # |1= The language code (see Wiktionary:Languages) for the language that the term is in. 
    # |sc= (optional) The script code (see Wiktionary:Scripts) for the script that the term is written in. 
    # |2=, |3= etc. parts of the words to show. Either: 1) At least one of the provided parts must begin and/or end with a hyphen (prefix, suffix, interfix); 2) or there must be two or more parts (it may be a compound, with or without prefixes, suffixes, interfixes).
    # |pos= The part of speech to include in the category names, in plural form. Defaults to words.
    # The following parameters are available for each matching part in the numbered/positional parameters. The N must be replaced by the corresponding part index. For example, for the second part (positional parameter 3), use 2 for N. Most of these parameters correspond directly to the equivalent parameters in the standard {{l}} (and {{m}}) template.
    # |altN= The alternative display form. Equivalent to the third parameter of {{l}}.
    # |tN= A gloss to show after the part. Equivalent to the fourth parameter of {{l}}. The parameter |glossN= is deprecated for this purpose.
    # |trN= The transliteration, as in {{l}}.
    # |tsN= The transcription, in languages where the transliteration and transcription differ markedly, as in {{l}}.
    # |gN= The gender (multiple comma-separated genders may be specified for a given part).
    # |idN= The sense id, as in {{l}}. As distinguished by mere linking templates, the affix template, categorizing terms by affix, also adds the sense id to the category name to distinguish various purposes of the same affix shape, hence the sense id in the dictionary entry for the affix should have a reasonable name in respect to this categorization. Changes the category name from language name terms affixed with affix to language name terms affixed with affix (value of id parameter).
    # |posN= The part of speech label to show after the part, as in {{l}}. If this parameter contains patronym(ic), the entry will be added to a language's patronymic category. If this parameter contains diminutive and the |pos= parameter is defined, the entry will be added to a diminutive part-of-speech category. For instance, the parameter values |pos=noun and |pos2=diminutive suffix will add an entry to the language's diminutive nouns category.
    # |litN= The literal meaning to show after the part, as in {{l}}.
    # |qN= Qualifier text to display after the part, in parens and normally italicized.
    # |langN= language code to use for this particular part. This overrides the default provided by |1=. When this is provided, the language name is displayed before the part, and a derivational category is also added to the entry. This is used for the occasional term which was directly affixed at the time of borrowing, and for which no native base form existed at the time, such as vexillology.
    # |scN= The script code to use for this particular part. This overrides the default provided by |sc=.

    '1': "language",
    "sc": "script code",
    '2': "prefix",
    '3': "root",
    "pos": "pos",
    "alt1": "alt prefix",
    "alt2": "alt root",
    "t1": "gloss prefix",
    "t2": "gloss root",
    "tr1": "transliteration prefix",
    "tr2": "transliteration root",
    "ts1": "transcription prefix",
    "ts2": "transcription root",
    "g1": "gender/number prefix", # XXX what about other gs?
    "g2": "gender/number root", # XXX what about other gs?
    "id1": "id prefix",
    "id2": "id root",
    "pos1": "pos prefix",
    "pos2": "pos root",
    "lit1": "translation prefix",
    "lit2": "translation root",
    "q1": "qualifier prefix",
    "q2": "qualifier root",
    "lang1": "language prefix",
    "lang2": "language root",
    "sc1": "script prefix",
    "sc2": "script root"
}

suffixArgsMap = {
    # When to use
    # This template is used in the etymology section. Use {{suffix|language code|root|suffix}}
    # where root is the root of the term and suffix is the suffix.

    # Parameters
    # |1= The language code (see Wiktionary:Languages) for the language that the term is in. 
    # |sc= (optional) The script code (see Wiktionary:Scripts) for the script that the term is written in. 
    # |2=, |3= etc. parts of the words to show. Either: 1) At least one of the provided parts must begin and/or end with a hyphen (prefix, suffix, interfix); 2) or there must be two or more parts (it may be a compound, with or without prefixes, suffixes, interfixes).
    # |pos= The part of speech to include in the category names, in plural form. Defaults to words.
    # The following parameters are available for each matching part in the numbered/positional parameters. The N must be replaced by the corresponding part index. For example, for the second part (positional parameter 3), use 2 for N. Most of these parameters correspond directly to the equivalent parameters in the standard {{l}} (and {{m}}) template.
    # |altN= The alternative display form. Equivalent to the third parameter of {{l}}.
    # |tN= A gloss to show after the part. Equivalent to the fourth parameter of {{l}}. The parameter |glossN= is deprecated for this purpose.
    # |trN= The transliteration, as in {{l}}.
    # |tsN= The transcription, in languages where the transliteration and transcription differ markedly, as in {{l}}.
    # |gN= The gender (multiple comma-separated genders may be specified for a given part).
    # |idN= The sense id, as in {{l}}. As distinguished by mere linking templates, the affix template, categorizing terms by affix, also adds the sense id to the category name to distinguish various purposes of the same affix shape, hence the sense id in the dictionary entry for the affix should have a reasonable name in respect to this categorization. Changes the category name from language name terms affixed with affix to language name terms affixed with affix (value of id parameter).
    # |posN= The part of speech label to show after the part, as in {{l}}. If this parameter contains patronym(ic), the entry will be added to a language's patronymic category. If this parameter contains diminutive and the |pos= parameter is defined, the entry will be added to a diminutive part-of-speech category. For instance, the parameter values |pos=noun and |pos2=diminutive suffix will add an entry to the language's diminutive nouns category.
    # |litN= The literal meaning to show after the part, as in {{l}}.
    # |qN= Qualifier text to display after the part, in parens and normally italicized.
    # |langN= language code to use for this particular part. This overrides the default provided by |1=. When this is provided, the language name is displayed before the part, and a derivational category is also added to the entry. This is used for the occasional term which was directly affixed at the time of borrowing, and for which no native base form existed at the time, such as vexillology.
    # |scN= The script code to use for this particular part. This overrides the default provided by |sc=.

    '1': "language",
    "sc": "script code",
    '2': "root",
    '3': "suffix",
    "pos": "pos",
    "alt2": "alt suffix",
    "alt1": "alt root",
    "t2": "gloss suffix",
    "t1": "gloss root",
    "tr2": "transliteration suffix",
    "tr1": "transliteration root",
    "ts2": "transcription suffix",
    "ts1": "transcription root",
    "g2": "gender/number suffix", # XXX what about other gs?
    "g1": "gender/number root", # XXX what about other gs?
    "id2": "id suffix",
    "id1": "id root",
    "pos2": "pos suffix",
    "pos1": "pos root",
    "lit2": "translation suffix",
    "lit1": "translation root",
    "q2": "qualifier suffix",
    "q1": "qualifier root",
    "lang2": "language suffix",
    "lang1": "language root",
    "sc2": "script suffix",
    "sc1": "script root"
}


argsMap = {
    # This template is intended specifically for loanwords that were borrowed 
    # during the time the borrowing language was spoken 
    'borrowed': borrowedArgsMap,

    # This template is a "catch-all" that is used when neither {{inherited}} 
    # nor {{borrowed}} is applicable.
    'derived': borrowedArgsMap,

    # This template generates a link to an entry in a given language. 
    # It links to a specific language-section on the target page, and applies language-specific 
    # formatting. It can also show a number of annotations after the linked term.
    'mention': mentionArgsMap,

    # This template is intended for terms that have an unbroken chain of inheritance 
    # from the source term in question.
    'inherited': borrowedArgsMap,

    # This template is used to format the etymology of terms cognate with terms in another language.
    'cognate': mentionArgsMap,

    # This template shows the parts (morphemes) that make up a word.
    'affix': affixArgsMap,

    # When to use
    # This template is used in the etymology section. Use {{prefix|language code|prefix|root}}
    # where prefix is the prefix, excluding hyphen, and root is the root of the term.
    'prefix': prefixArgsMap,

    # This template is used in the etymology section. Use {{suffix|language code|root|suffix}}
    # where root is the root of the term and suffix is the suffix.
    'suffix': suffixArgsMap,

    # Use this template in an etymology section of doublets (such as fire and pyre).
    'doublet': affixArgsMap,

    # This template is used for terms derived from Proto-Indo-European roots.
    'PIE root': affixArgsMap,

    # For use in the Etymology sections of words which consist of only a prefix and a suffix, 
    # or which were formed by simultaneous application of a prefix and a suffix to some other element(s).
    'confix': affixArgsMap,

    # Use this template in an etymology section of back-formations.
    'back-form': mentionArgsMap,

    # This template indicates that a term originated as a calque (also called a 
    # loan translation) of a term in another language. 
    'calque': borrowedArgsMap,

    # This template indicates that a term originated as a calque (also called a 
    # loan translation) of a term in another language. 
    'clipping': mentionArgsMap,

    # This template indicates that a term originated as a calque (also called a 
    # loan translation) of a term in another language. 
    'lbor': borrowedArgsMap,
    'learned borrowing': borrowedArgsMap, # XXX lbor is not getting picked up in the shortcut map, why?

    # This template indicates that a term originated as a calque (also called a 
    # loan translation) of a term in another language. 
    'onomatopoeic': mentionArgsMap
}

ignored_templates = ignored_templates - etymologyTemplates

# This dictionary maps section titles in articles to parts-of-speech.  There
# is a lot of variety and misspellings, and this tries to deal with those.
pos_map = {
    "abbreviation": "abbrev",
    "acronym": "abbrev",
    "adjectival": "adj_noun",
    "adjectival noun": "adj_noun",
    "adjectival verb": "adj_verb",
    "adjective": "adj",
    "adjectuve": "adj",
    "adjectives": "adj",
    "adverb": "adv",
    "adverbs": "adv",
    "adverbial phrase": "adv_phrase",
    "affix": "affix",
    "adjective suffix": "affix",
    "article": "article",
    "character": "character",
    "circumfix": "circumfix",
    "circumposition": "circumpos",
    "classifier": "classifier",
    "clipping": "abbrev",
    "clitic": "clitic",
    "command form": "cmd",
    "command conjugation": "cmd_conj",
    "combining form": "combining_form",
    "comparative": "adj_comp",
    "conjunction": "conj",
    "conjuntion": "conj",
    "contraction": "abbrev",
    "converb": "converb",
    "counter": "counter",
    "determiner": "det",
    "diacritical mark": "character",
    "enclitic": "clitic",
    "enclitic particle": "clitic",
    "gerund": "gerund",
    "glyph": "character",
    "han character": "character",
    "han characters": "character",
    "ideophone": "noun",  # XXX
    "infix": "infix",
    "infinitive": "participle",
    "initialism": "abbrev",
    "interfix": "interfix",
    "interjection": "intj",
    "interrogative pronoun": "pron",
    "intransitive verb": "verb",
    "instransitive verb": "verb",
    "letter": "letter",
    "ligature": "character",
    "label": "character",
    "nom character": "character",
    "nominal nuclear clause": "clause",
    "νoun": "noun",
    "nouɲ": "noun",
    "noun": "noun",
    "nouns": "noun",
    "noum": "noun",
    "number": "num",
    "numeral": "num",
    "ordinal number": "ordinal",
    "participle": "participle",  # XXX
    "particle": "particle",
    "past participle": "participle",  # XXX
    "perfect expression": "participle",  # XXX
    "perfection expression": "participle",  # XXX
    "perfect participle": "participle",  # XXX
    "personal pronoun": "pron",
    "phrasal verb": "phrasal_verb",
    "phrase": "phrase",
    "phrases": "phrase",
    "possessive determiner": "det",
    "possessive pronoun": "det",
    "postposition": "postp",
    "predicative": "predicative",
    "prefix": "prefix",
    "preposition": "prep",
    "prepositions": "prep",
    "prepositional expressions": "prep",
    "prepositional phrase": "prep_phrase",
    "prepositional pronoun": "pron",
    "present participle": "participle",
    "preverb": "verb",
    "pronoun": "pron",
    "proper noun": "name",
    "proper oun": "name",
    "proposition": "prep",  # Appears to be a misspelling of preposition
    "proverb": "proverb",
    "punctuation mark": "punct",
    "punctuation": "punct",
    "relative": "conj",
    "root": "root",
    "syllable": "character",
    "suffix": "suffix",
    "suffix form": "suffix",
    "symbol": "symbol",
    "transitive verb": "verb",
    "verb": "verb",
    "verbal noun": "noun",
    "verbs": "verb",
    "digit": "digit",   # I don't think this is actually used in Wiktionary
}

# Set of all possible parts-of-speech returned by wiktionary reading.
PARTS_OF_SPEECH = set(pos_map.values())

# Templates ({{name|...}}) that will be replaced by the value of their
# first argument when cleaning up titles/values.
clean_arg1_tags = [
    "...",
    "Br. English form of",
    "W",
    "Wikipedia",
    "abb",
    "abbreviation of",
    "abbreviation",
    "acronym of",
    "agent noun of",
    "alt form of",
    "alt form",
    "alt form",
    "alt-form",
    "alt-sp",
    "altcaps",
    "alternate form of",
    "alternate spelling of",
    "alternative capitalisation of",
    "alternative capitalization of",
    "alternative case form of",
    "alternative form of",
    "alternative name of",
    "alternative name of",
    "alternative plural of",
    "alternative spelling of",
    "alternative term for",
    "alternative typography of",
    "altform",
    "altspell",
    "altspelling",
    "apocopic form of",
    "archaic form of",
    "archaic spelling of",
    "aspirate mutation of",
    "attributive form of",
    "attributive of",
    "caret notation of",
    "clip",
    "clipping of",
    "clipping",
    "common misspelling of",
    "comparative of",
    "contraction of",
    "dated form of",
    "dated spelling of",
    "deliberate misspelling of",
    "diminutive of",
    "ellipsis of",
    "ellipse of",
    "elongated form of",
    "en-archaic second-person singular of",
    "en-archaic third-person singular of",
    "en-comparative of",
    "en-irregular plural of",
    "en-past of",
    "en-second person singular past of",
    "en-second-person singular past of",
    "en-simple past of",
    "en-superlative of",
    "en-third person singular of",
    "en-third-person singular of",
    "euphemistic form of",
    "euphemistic spelling of",
    "eye dialect of",
    "eye dialect",
    "eye-dialect of",
    "femine of",
    "feminine noun of",
    "feminine plural of",
    "feminine singular of",
    "form of",
    "former name of",
    "gerund of",
    "hard mutation of",
    "honoraltcaps",
    "imperative of",
    "informal form of"
    "informal spelling of",
    "ja-l",
    "ja-r",
    "lenition of",
    "masculine plural of",
    "masculine singular of",
    "misconstruction of",
    "misspelling of",
    "mixed mutation of",
    "n-g",
    "native or resident of",
    "nb...",
    "neuter plural of",
    "neuter singular of",
    "ngd",
    "nobr",
    "nominative plural of",
    "non-gloss definition",
    "non-gloss",
    "nonstandard form of",
    "nonstandard spelling of",
    "nowrap",
    "obsolete form of",
    "obsolete spelling of",
    "obsolete typography of",
    "overwrite",
    "past of",
    "past sense of",
    "past tense of",
    "pedlink",
    "pedlink",
    "plural form of",
    "plural of",
    "present of",
    "present particle of",
    "present tense of",
    "pronunciation spelling of",
    "pronunciation spelling",
    "pronunciation respelling of",
    "rare form of",
    "rare spelling of",
    "rareform",
    "second person singular past of",
    "second-person singular of",
    "second-person singular past of",
    "short for",
    "short form of",
    "short of",
    "singular form of",
    "singular of",
    "slim-wikipedia",
    "soft mutation of",
    "standard form of",
    "standard spelling of",
    "standspell",
    "sub",
    "sup",
    "superlative of",
    "superseded spelling of",
    "swp",
    "taxlink",
    "taxlinknew",
    "uncommon spelling of",
    "unsupported",
    "verb",
    "vern",
    "w",
    "wikipedia",
    "wikisaurus",
    "wikispecies",
    "zh-m",
]

# Templates that will be replaced by their second argument when cleaning up
# titles/values.
clean_arg2_tags = [
    "zh-l",
    "ja-l",
    "l",
    "defn",
    "w",
    "m",
    "mention",
]

# Templates that will be replaced by their third argument when cleaning up
# titles/values.
clean_arg3_tags = [
    "w2",
]

# Templates that will be replaced by a value when cleaning up titles/values.
# The replacements may refer to the first argument of the template using \1.
#
# Note that there is a non-zero runtime cost for each replacement in this
# dictionary; keep its size reasonable.
clean_replace_map = {
    "en dash": " - ",
    "em dash": " - ",
    "ndash": " - ",
    "\\": " / ",
    "...": "...",
    "BCE": "BCE",
    "B.C.E.": "B.C.E.",
    "CE": "CE",
    "C.E.": "C.E.",
    "BC": "BC",
    "B.C.": "B.C.",
    "A.D.": "A.D.",
    "AD": "AD",
    "Latn-def": "latin character",
    "sumti": r"x\1",
    "inflection of": r"inflection of \1",
    "initialism of": r"initialism of \1",
    "synonym of": r"synonym of \1",
    "given name": r"\1 given name",
    "forename": r"\1 given name",
    "historical given name": r"\1 given name",
    "surname": r"surname",
    "taxon": r"taxonomic \1",
    "SI-unit": "unit of measurement",
    "SI-unit-abb2": "unit of measurement",
    "SI-unit-2": "unit of measurement",
    "SI-unit-np": "unit of measurement",
    "gloss": r"(\1)",
}

# Note: arg_re contains two sets of parenthesis
arg_re = (r"(\|[-_a-zA-Z0-9]+=[^}|]+)*"
          r"\|(([^|{}]|\{\{[^}]*\}\}|\[\[[^]]+\]\]|\[[^]]+\])*)")

# Matches more arguments and end of template
args_end_re = r"(" + arg_re + r")*\}\}"

# Regular expression for replacing templates by their arg1.  arg1 is \3
clean_arg1_re = re.compile(r"(?s)\{\{(" +
                           "|".join(re.escape(x) for x in clean_arg1_tags) +
                           r")" +
                           arg_re + args_end_re)

# Regular expression for replacing templates by their arg2.  arg2 is \4
clean_arg2_re = re.compile(r"(?s)\{\{(" +
                           "|".join(re.escape(x) for x in clean_arg2_tags) +
                           r")" + arg_re + arg_re + args_end_re)

# Regular expression for replacing templates by their arg3.  arg3 is \6
clean_arg3_re = re.compile(r"(?s)\{\{(" +
                           "|".join(re.escape(x) for x in clean_arg3_tags) +
                           r")" + arg_re + arg_re + arg_re + args_end_re)

# Mapping from German verb form arguments to "canonical" values in
# word sense tags."""
de_verb_form_map = {
    # Keys under which to look for values
    "_keys": [2, 3, 4, 5, 6, 7, 8, 9],
    # Mapping of values in arguments to canonical values
    "1": ["1"],
    "2": ["2"],
    "3": ["3"],
    "pr": ["present participle"],
    "pp": ["past participle"],
    "i": ["imperative"],
    "s": ["singular"],
    "p": ["plural"],
    "g": ["present"],
    "v": ["past"],
    "k1": ["subjunctive 1"],
    "k2": ["subjunctive 2"],
}

# Mapping from Spanish verb form values to "canonical" values."""
es_verb_form_map = {
    # Argument names under which we search for values.
    "_keys": ["mood", "tense", "num", "number", "pers", "person", "formal",
              "sense", "sera", "gen", "gender"],
    # Mapping of values in arguments to canonical values
    "ind": ["indicative"],
    "indicative": ["indicative"],
    "subj": ["subjunctive"],
    "subjunctive": ["subjunctive"],
    "imp": ["imperative"],
    "imperative": ["imperative"],
    "cond": ["conditional"],
    "par": ["past participle"],
    "part": ["past participle"],
    "participle": ["past participle"],
    "past-participle": ["past participle"],
    "past participle": ["past participle"],
    "adv": ["present participle"],
    "adverbial": ["present participle"],
    "ger": ["present participle"],
    "gerund": ["present participle"],
    "gerundive": ["present participle"],
    "gerundio": ["present participle"],
    "present-participle": ["present participle"],
    "present participle": ["present participle"],
    "pres": ["present"],
    "present": ["present"],
    "pret": ["preterite"],
    "preterit": ["preterite"],
    "preterite": ["preterite"],
    "imp": ["past"],
    "imperfect": ["past"],
    "fut": ["future"],
    "future": ["future"],
    "cond": ["conditional"],
    "conditional": ["conditional"],
    "s": ["singular"],
    "sing": ["singular"],
    "singular": ["singular"],
    "p": ["plural"],
    "pl": ["plural"],
    "plural": ["plural"],
    "1": ["1"],
    "first": ["1"],
    "first-person": ["1"],
    "2": ["2"],
    "second": ["2"],
    "second person": ["2"],
    "second-person": ["2"],
    "3": ["3"],
    "third": ["3"],
    "third person": ["3"],
    "third-person": ["3"],
    "y": ["formal"],
    "yes": ["formal"],
    "no": ["not formal"],
    "+": ["affirmative"],
    "aff": ["affirmative"],
    "affirmative": ["affirmative"],
    "-": ["negative"],
    "neg": ["negative"],
    "negative": ["negative"],
    "se": ["se"],
    "ra": ["ra"],
    "m": ["masculine"],
    "masc": ["masculine"],
    "masculine": ["masculine"],
    "f": ["feminine"],
    "fem": ["feminine"],
    "feminine": ["feminine"],
}


# Mapping from a template name (without language prefix) for the main word
# (e.g., fi-noun, fi-adj, en-verb) to permitted parts-of-speech in which
# it could validly occur.  This is used as just a sanity check to give
# warnings about probably incorrect coding in Wiktionary.
template_allowed_pos_map = {
    "abbr": ["abbrev"],
    "abbr": ["abbrev"],
    "noun": ["noun", "abbrev", "pron", "name", "num"],
    "plural noun": ["noun", "name"],
    "proper noun": ["noun", "name", "proper-noun"],
    "proper-noun": ["name", "noun", "proper-noun"],
    "verb": ["verb", "phrase"],
    "plural noun": ["noun"],
    "adv": ["adv"],
    "particle": ["adv", "particle"],
    "adj": ["adj"],
    "pron": ["pron", "noun"],
    "name": ["name", "noun", "proper-noun"],
    "adv": ["adv", "intj", "conj", "particle"],
    "phrase": ["phrase"],
}


# Corrections for misspelled section titles.  This basically maps the actual
# subsection title to the title that will be used when we parse it.  We should
# really review and fix all Wiktionary entries that use these, especially the
# misspellings.  In some cases we should improve the code to handle the
# additional information provided by the section title (e.g., gender).
# XXX do that later.
sectitle_corrections = {
    "adjectif": "adjective",
    "alernative forms": "alternative forms",
    "antonyid": "antonyms",
    "antoynms": "antonyms",
    "conjugaton 1": "declension",  # XXX
    "conjugaton 2": "declension",  # XXX
    "coordinate terid": "coordinate terms",
    "decelsnion": "declension",
    "decentants": "descendants",
    "declension (fem.)": "declension",  # XXX should utilize this
    "declension (masc.)": "declension",  # XXX should utilize this
    "declension (neut.)": "declension",  # XXX should utilize this
    "declension (person)": "declension",  # XXX
    "declension for adjectives": "declension",
    "declension for feminine": "declension",  # XXX
    "declension for nouns": "declension",
    "declension for sense 1 only": "declension",  # XXX
    "declension for sense 2 only": "declension",  # XXX
    "declension for words with singular and plural": "declension",  # XXX
    "declension for words with singular only": "declension",  # XXX
    "declination": "declension",
    "deived terms": "derived terms",
    "derived teerms": "derived terms",
    "derived temrs": "derived terms",
    "derived terrms": "derived terms",
    "derived words": "derived terms",
    "derivedt terms": "derived terms",
    "deriveed terms": "derived terms",
    "derivered terms": "derived terms",
    "etimology": "etymology",
    "etymlogy": "etymology",
    "etymology2": "etymology",
    "expresion": "expression",
    "feminine declension": "declension",  # XXX
    "holonyid": "holonyms",
    "hypernym": "hypernyms",
    "hyponyid": "hyponyms",
    "inflection 1 (fem.)": "declension",  # XXX
    "inflection 1 (way)": "declension",  # XXX
    "inflection 2 (neut.)": "declension",  # XXX
    "inflection 2 (time)": "declension",  # XXX
    "inflection": "declension",
    "masculine declension": "declension",  # XXX
    "nouns and adjective": "noun",  # XXX not really correct
    "nouns and adjectives": "noun",   # XXX this isn't really correct
    "nouns and other parts of speech": "noun",   # XXX not really correct
    "opposite": "antonyms",
    "participles": "verb",
    "pronounciation": "pronunciation",
    "pronuncation": "pronunciation",
    "pronunciaion": "pronunciation",
    "pronunciation and usage notes": "pronunciation",
    "pronunciationi": "pronunciation",
    "pronunciations": "pronunciation",
    "pronunciaton": "pronunciation",
    "pronunciayion": "pronunciation",
    "pronuniation": "pronunciation",
    "pronunciation 1": "pronunciation",
    "pronunciation 2": "pronunciation",
    "pronunciation 3": "pronunciation",
    "pronunciation 4": "pronunciation",
    "quptations": "quotations",
    "realted terms": "related terms",
    "refereces": "references",
    "referenes": "references",
    "refererences": "references",
    "referneces": "references",
    "refernecs": "references",
    "related names": "related terms",
    "related terid": "related terms",
    "synomyms": "synonyms",
    "synonmys": "synonyms",
    "synonym": "synonyms",
    "synonymes": "synonyms",
    "syonyms": "synonyms",
    "syonynms": "synonyms",
    "usagw note": "usage note",
}