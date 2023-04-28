#!/usr/bin/python3
"""0-lockboxes."""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    ----------------------------------------
    boxes: is a list of lists

    a key with the same number as a box opens that box.
    """
    det = {}
    idx = 0

    for box in boxes:
        if len(box) == 0 or idx == 0:
            det[idx] = -1
        for key in box:
            if (key < len(boxes)) and (key != idx):
                det[key] = key
        if (len(det) == len(boxes)):
            return True
        idx += 1
    return False
