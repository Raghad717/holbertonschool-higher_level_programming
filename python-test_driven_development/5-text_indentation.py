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

    # Special case for empty string
    if text == "":
        print("", end="")
        return

    # Process character by character
    i = 0
    length = len(text)
    
    while i < length:
        # Print current character
        print(text[i], end="")
        
        # If it's one of our special characters, add two newlines
        if text[i] in ".?:":
            print("\n")
            # Skip any spaces immediately after the punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            # Continue to next iteration without incrementing i again
            continue
        
        i += 1
