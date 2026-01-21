#!/usr/bin/python3
"""
Text Indentation Module
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        char = text[i]

        print(char, end="")  # print current char

        if char in ".?:":
            # skip spaces after punctuation
            i += 1
            while i < n and text[i] == " ":
                i += 1
            # only print newlines if next char exists and is not punctuation
            if i < n and text[i] not in ".?:\n":
                print("\n\n", end="")
            continue

        i += 1
