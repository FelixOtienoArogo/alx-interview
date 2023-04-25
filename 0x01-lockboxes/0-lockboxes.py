#!/usr/bin/python3
"""0-lockboxes."""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    ----------------------------------------
    boxes: is a list of lists

    a key with the same number as a box opens that box.
    """
    det = True
    for box in boxes:
        for key in box:
            if len(boxes[key - 1]) > 0:
                det = True
            else:
                det = False
                return det
    return det
