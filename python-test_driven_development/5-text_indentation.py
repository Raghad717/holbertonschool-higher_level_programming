#!/usr/bin/python3
"""
Text Indentation Module
Prints a text with 2 new lines after each '.', '?' or ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', or ':' using only two print statements.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""  # buffer to hold final formatted text
    skip_space = False

    for char in text:
        if char in ".?:":
            result += char + "\n\n"  # add punctuation + 2 newlines
            skip_space = True
        else:
            if skip_space and char == " ":
                continue  # skip spaces immediately after punctuation
            result += char
            skip_space = False

    print(result.strip())  # first print: the whole formatted text
