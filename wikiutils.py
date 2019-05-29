import re
import html
from definitions import *

def remove_html_comments(text):
    """Removes HTML comments from the value."""
    assert isinstance(text, str)
    text = text.strip()
    text = re.sub(r"(?s)<!--.*?-->", "", text)
    return text


def clean_value(title):
    """Cleans a title or value into a normal string.  This should basically
    remove any Wikimedia formatting from it: HTML tags, templates, links,
    emphasis, etc.  This will also merge multiple whitespaces into one
    normal space and will remove any surrounding whitespace."""
    # Remove HTML comments
    title = re.sub(r"(?s)<!--.*?-->", "", title)
    # Replace tags for which we have replacements.
    for k, v in clean_replace_map.items():
        if v.find("\\") < 0:
            title = re.sub(r"\{\{" + re.escape(k) +
                           r"(" + arg_re + r")*\}\}", v, title)
        else:
            v = re.sub(r"\\2", r"\\7", v)
            v = re.sub(r"\\1", r"\\4", v)
            title = re.sub(r"\{\{" + re.escape(k) +
                           r"((" + arg_re + r")" +
                           r"(" + arg_re + r")?)?" +
                           r"(" + arg_re + r")*" +
                           r"\}\}",
                           v, title)
    # Replace tags by their arguments.  Note that they may be nested, so we
    # keep repeating this until there is no change.  The regexps can only
    # handle one level of nesting (i.e., one template inside another).
    while True:
        orig = title
        title = re.sub(clean_arg3_re, r"\9", title)
        title = re.sub(clean_arg2_re, r"\6", title)
        title = re.sub(clean_arg1_re, r"\3", title)
        if title == orig:
            break
    # Remove any remaining templates.
    title = re.sub(r"\{\{[^}]+\}\}", "", title)
    # Remove references (<ref>...</ref>).
    title = re.sub(r"(?s)<ref>.*?</ref>", "", title)
    # Replace <br/> by comma space (it is used to express alternatives in some
    # declensions)
    title = re.sub(r"(?s)<br/?>", ", ", title)
    # Remove any remaining HTML tags.
    title = re.sub(r"(?s)<[^>]+>", "", title)
    # Replace links with [[...|...]] by their only or second argument
    title = re.sub(r"\[\[(([^]|]+\|)?)([^]|]+?)\]\]", r"\3", title)
    # Replace HTML links [url display] (with space) by the display value.
    title = re.sub(r"\[[^ ]+?\s+([^]]+?)\]", r"\1", title)
    # Replace remaining HTML links by the URL.
    title = re.sub(r"\[([^]]+)\]", r"\1", title)
    # Replace various empases (quoted text) by its value.
    title = re.sub(r"''+(([^']|'[^'])+?)''+", r"\1", title)
    # Replace HTML entities
    title = html.unescape(title)
    title = re.sub("\xa0", " ", title)  # nbsp
    # This unicode quote seems to be used instead of apostrophe quite randomly
    # (about 4% of apostrophes in English entries, some in Finnish entries).
    title = re.sub("\u2019", "'", title)  # Note: no r"..." here!
    # Replace strange unicode quotes with normal quotes
    title = re.sub(r"”", '"', title)
    # Replace whitespace sequences by a single space.
    title = re.sub(r"\s+", " ", title)
    # Remove whitespace before periods and commas etc
    title = re.sub(r" ([.,;:!?)])", r"\1", title)
    # Strip surrounding whitespace.
    title = title.strip()
    return title


def split_subsections(text):
    """Split the text into a linear sequence of sections.  Note that we
    ignore the nesting structure of subtitles, since that seems to be
    poorly enforced in Wiktionary.  This returns a list of (subtitle,
    text).  The subtitle has been fully cleaned, and HTML comments
    have been removed from the text."""
    # Remove HTML comments from the whole page.  We want to do this before
    # analyzing subsections, as they could be commented out.
    text = remove_html_comments(text)
    # Find start and end offsets and titles for all subsections
    regexp = r"(?s)(^|\n)==+([^=\n]+?)==+"
    offsets = list((m.start(), m.end(), clean_value(m.group(2)))
                   for m in re.finditer(regexp, text))
    # Add a dummy section at end of text.
    offsets.append((len(text), len(text), ""))
    # Create first subsection from text before the first subtitle
    subsections = []
    first = text[:offsets[0][0]]
    if first:
        subsections.append(("", first))
    # Add all other subsections (except the dummy one)
    for i in range(len(offsets) - 1):
        titlestart, start, subtitle = offsets[i]
        # Get end offset from the entry for the next subsection
        end = offsets[i + 1][0]
        # Clean the section title
        subtitle = clean_value(subtitle)
        # Add an entry for the subsection.
        subsection = text[start: end]
        subsections.append((subtitle, subsection))
    return subsections


def data_append(data, key, value):
    """Appends ``value`` under ``key`` in the dictionary ``data``.  The key
    is created if it does not exist."""
    assert isinstance(data, dict)
    assert isinstance(key, str)
    lst = data.get(key, [])
    lst.append(value)
    if lst:
        data[key] = lst


def data_extend(data, key, values):
    """Appends all values in a list under ``key`` in the dictionary ``data``."""
    assert isinstance(data, dict)
    assert isinstance(key, str)
    assert isinstance(values, (list, tuple))
    lst = data.get(key, [])
    lst.extend(values)
    if lst:
        data[key] = lst


def template_args_to_dict(t):
    """Returns a dictionary containing the template arguments.  This is
    typically used when the argument dictionary will be returned from the
    parsing.  Positional arguments will be keyed by numeric strings.
    The name of the template will be added under the key "template_name"."""
    ht = {}
    for x in t.arguments:
        name = x.name.strip()
        value = x.value
        ht[name] = clean_value(value)
    ht["template_name"] = t.name.strip()
    return ht


def clean_quals(vec):
    """Extracts and cleans qualifier values from the vector of arguments.
    Qualifiers are generally usage or other notes such as "archaic",
    "colloquial", "chemistry", "british", etc.  There is no standard set
    of values for them and the set probably varies from language to
    language."""
    assert isinstance(vec, (list, tuple))
    for x in vec:
        assert isinstance(x, str)

    tags = []
    for i in range(len(vec)):
        x = vec[i]
        i += 1
        if x in ("en", "fi"):
            # If the qualifiers are from a template that has language tags,
            # those hould be removed from the vector before passing it to
            # this function.  This warning indicates the caller probably
            # forgot to remove the language tag.
            print("clean_quals: WARNING: {} in vec: {}".format(x, vec))
            continue
        # Certain modifiers are often written as separate arguments but
        # actually modify the following value.  We combine them with the
        # following value using a space.
        while (i < len(vec) - 1 and
               vec[-1] in ("usually", "often", "rarely", "strongly",
                           "extremely", "including",
                           "chiefly", "sometimes", "mostly", "with", "now")):
            x += " " + vec[i]
            i += 1
        # Values may be combined using "and" and "or" or "_".  We replace
        # all these by a space and combine.
        while (i < len(vec) - 2 and
               vec[i] in ("_", "and", "or")):
            x += " " + vec[i + 1]
            i += 2
        tags.append(x)
    return tags


def t_vec(t):
    """Returns a list containing positional template arguments.  Empty strings
    will be added for any omitted arguments.  The vector will include the last
    non-empty supplied argument, but not values beyond it."""
    vec = []
    for i in range(1, 20):
        v = t_arg(t, i)
        vec.append(v)
    while vec and not vec[-1]:
        vec.pop()
    return vec


def t_arg(t, arg):
    """Retrieves argument ``arg`` from the template.  The argument may be
    identified either by its number or a string name.  Positional argument
    numbers start at 1.  This returns the empty string for arguments that
    don't exist.  The argument value is cleaned before returning."""
    # If the argument specifier is an integer, convert it to a string.
    if isinstance(arg, int):
        arg = str(arg)
    assert isinstance(arg, str)
    # Get the argument value from the template.
    v = t.get_arg(arg)
    # If it does not exist, return empty string.
    if v is None:
        return ""
    # Otherwise clean the value.
    return clean_value(v.value)


def verb_form_map_fn(word, data, name, t, form_map):
    """Maps values in a language-specific verb form map into values for "tags"
    that are reasonably uniform across languages.  This also deals with a
    lot of misspellings and inconsistencies in how the values are entered in
    Wiktionary.  ``data`` here is the word sense."""
    # Add an indication that the word sense is a form of an other word.
    data_append(data, "form_of", t_arg(t, 1))
    # Iterate over the specified keys in the template.
    for k in form_map["_keys"]:
        v = t_arg(t, k)
        if not v:
            continue
        # Got a value for key.  Now map the value.  Each entry in the
        # dictionary should be a list of tags to add.
        if v in form_map:
            lst = form_map[v]
            assert isinstance(lst, (list, tuple))
            for x in lst:
                assert isinstance(x, str)
                data_append(data, "tags", x)
        else:
            print(word, "UNKNOWN VERB FORM KEY", k, "IN", name, "of:",
                  v, "in:", str(t))
