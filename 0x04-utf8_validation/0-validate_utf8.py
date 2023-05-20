#!/usr/bin/python3
"""validUTF8."""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    valid = False
    for i in range(len(data)):
        char = data[i]
        msb = char >> 7
        if msb == 1:
            msb = char >> 5
            if msb ^ 6 == 0:
                msb2 = data[i + 1] >> 6
                if msb2 ^ 2 == 0:
                    valid = True
                    i += 2
                else:
                    return False
            else:
                msb = char >> 4
                if msb ^ 14 == 0:
                    try:
                        msb2 = data[i + 1] >> 6
                        msb3 = data[i + 2] >> 6
                    except Exception:
                        return False
                    if msb2 ^ 2 == 0 and msb3 ^ 2 == 0:
                        valid = True
                        i += 3
                    else:
                        return False
                else:
                    msb = char >> 3
                    if msb ^ 30 == 0:
                        try:
                            msb2 = data[i + 1] >> 6
                            msb3 = data[i + 2] >> 6
                            msb4 = data[i + 3] >> 6
                        except Exception:
                            return False
                        if msb2 ^ 2 == 0 and msb3 ^ 2 == 0 and msb4 ^ 2 == 0:
                            valid = True
                            i += 4
                        else:
                            return False
        elif msb ^ 0 == 0:
            valid = True
    return valid
