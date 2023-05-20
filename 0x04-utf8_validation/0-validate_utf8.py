#!/usr/bin/python3
"""validUTF8."""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    mask = 1 << 7
    for char in data:
        if (mask & char) != 0:
            return False
    return True
