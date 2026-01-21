#!/usr/bin/python3
"""
Text Indentation Module
Prints a text with 2 new lines after each '.', '?' or ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', or ':'.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False
    n = len(text)

    for i, char in enumerate(text):
        if char in ".?:":
            print(char, end="")
            # Only add two newlines if next char exists and is not punctuation
            if i + 1 < n and text[i + 1] not in ".?:\n":
                print("\n\n", end="")
            else:
                print("", end="")  # Don't add extra newlines
            skip_space = True
        else:
            if skip_space and char == " ":
                continue
            print(char, end="")
            skip_space = False
