#!/usr/bin/python3
"""Lockboxes challenge - determine if all boxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else False."""
    n = len(boxes)
    unlocked = set([0])
    queue = [0]
    while queue:
        box = queue.pop()
        for key in boxes[box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                queue.append(key)
    return len(unlocked) == n
