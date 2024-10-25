#!/usr/bin/python3
"""Determines if all boxes can be unlocked given a list of lists where each list contains keys to other boxes."""

def canUnlockAll(boxes):
    """Checks if all boxes in the list can be unlocked.

       Args:
           boxes (list of lists): Each list contains keys to other boxes.

       Returns:
           bool: True if all boxes can be unlocked, otherwise False.
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
