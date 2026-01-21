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
        # skip leading spaces
        while i < n and text[i] == " ":
            i += 1
        if i >= n:
            break

        char = text[i]
        print(char, end="")  # print current char

        if char in ".?:":
            print("\n\n", end="")  # 2 newlines after punctuation
            i += 1
            # skip spaces after punctuation
            while i < n and text[i] == " ":
                i += 1
            continue

        i += 1
