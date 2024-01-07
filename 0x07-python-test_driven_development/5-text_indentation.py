#!/usr/bin/python3
"""
    Module: text_indentation
    This module provides a function text_indentation(text)
    prints a square.
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text:

    Returns:
        None
    """
    txt = ""
    for i, ch in enumerate(text):
        if txt == " ":
            txt = ""
            continue
        print(ch, end="")
        if ch == "." or ch == ":" or ch == "?":
            if i + 1 < len(text):
                txt = text[i + 1]
            print("\n")
