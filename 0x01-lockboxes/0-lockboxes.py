#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    This function iterates over a list of lists (boxes), where each list
    represents a box and contains keys to other boxes. It starts with the
    first box unlocked (box 0) and iterates through the keys in each box.
    If a key corresponds to a box that hasn't been unlocked yet, it's added
    to the list of keys. If all boxes can be unlocked, the function returns
    True; otherwise, it returns False.

    Parameters:
    boxes (list of lists): Each list represents a box and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, else False.
    """
    keys = [0]
    for key in keys:
        for box_key in boxes[key]:
            if box_key not in keys and box_key < len(boxes):
                keys.append(box_key)
    if len(keys) == len(boxes):
        return True
    return False
