#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length of the string and its first character.
    If the string is empty, first character is None.
    """
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
