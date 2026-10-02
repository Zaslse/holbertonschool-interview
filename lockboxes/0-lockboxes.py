#!/usr/bin/python3
"""Module for determining whether all boxes can be unlocked."""


def canUnlockAll(boxes):
    """Return True if all boxes can be unlocked, otherwise False."""
    if not boxes:
        return True

    unlocked = {0}
    keys = [0]

    while keys:
        box = keys.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)
