#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determine if all boxes can be opened."""
    number_of_boxes = len(boxes)
    unlocked_boxes = [False] * number_of_boxes
    unlocked_boxes[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < number_of_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
