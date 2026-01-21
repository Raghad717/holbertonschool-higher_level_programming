#!/usr/bin/python3
"""
Text Indentation Module

This module provides a function to format text by adding two new lines
after each '.', '?', or ':' character and removing trailing/leading spaces.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', or ':' character.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None: The function prints the formatted text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    n = len(text)

    while i < n:
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result.strip(' '), end='')
