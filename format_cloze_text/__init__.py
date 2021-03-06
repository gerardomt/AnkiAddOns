"""This add-on add two filters

- mi-cloze: Cloze the text between square brackets [[ ]]
  
  {{mi-cloze:field}}


- cloze-format: Takes the text between square brackets and enclose it
in a tag <span class="cloze"></span>

  {{cloze-forma:field}}


They are used in the template of VocabularyContext notes to create
cards in the next manner:

=====================================================================
|                           Elogiar                                 |
|-------------------------------------------------------------------|
|"′Classic′ - a book which people [..] and don't read." - Mark Twain |
|                                                                   |
|-------------------------------------------------------------------|
|                           Praise                                  |
=====================================================================

=====================================================================
|"′Classic′ - a book which people PRAISE and don't read."  - Mark Twain|
|                                                                   |
|-------------------------------------------------------------------|
|                           Elogiar                                 |
=====================================================================

This add-on is NOT compatible with AnkiDroid


** To-Do **
- Add button and hotkey to enclose text between square brackets
- Make it compatible with AnkiDroid

"""

from anki import hooks
from anki.template import TemplateRenderContext

def format_cloze_text(field_text, field_name, filter_name, context):
    """This function is call each time a custom filter is encountered"""
    if filter_name == "mi-cloze":
        return mi_cloze(field_text)

    elif filter_name == "cloze-format":
        return cloze_format(field_text)

    return field_text


def mi_cloze(text):
    """Substitute the text between square brackets by [..]"""
    prefix, cloze, suffix = get_cloze_text(text)

    return prefix + ' <span class="cloze">[..]</span> ' + suffix


def cloze_format(text):
    """Enclose the text between square brackets with <span
    class"cloze"></span>

    """
    prefix, cloze, suffix = get_cloze_text(text)

    return prefix + '<span class="cloze">' + cloze + '</span>' + suffix


def get_cloze_text(text):
    """Separate the text in the text before [[, the text between [[ and
    ]], and the text after ]]

    """
    n = text.find("[[")
    m = text.find("]]")

    return text[:n], text[n+2 : m], text[m+2:]


hooks.field_filter.append(format_cloze_text)
