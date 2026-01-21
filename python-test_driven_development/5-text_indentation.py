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

    Examples:
        >>> text_indentation("Hello. World")
        Hello.
        <BLANKLINE>
        <BLANKLINE>
        World
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process the text
    i = 0
    result = ""
    length = len(text)
    
    while i < length:
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            # Skip any spaces immediately after the punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
    
    # Print the result without trailing spaces for each line
    lines = result.split('\n')
    for line in lines:
        print(line.strip(' '), end='' if line == lines[-1] else '\n')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
