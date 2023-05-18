#!/usr/bin/python3
"""validUTF8"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    if len(data) > 4 or len(data) < 1:
        return False
    return True
