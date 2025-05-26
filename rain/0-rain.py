#!/usr/bin/python3
"""Calculate the amount of rain that will be trapped after it rains
"""


def rain(walls):
    """Calculate how much rain will be trapped after it rains
    """
    if not walls or len(walls) < 3:
        return 0

    rain = 0
    for i in range(1, len(walls) - 1):
        left = max(walls[:i])
        right = max(walls[i + 1:])
        min_wall = min(left, right)
        if walls[i] < min_wall:
            rain += min_wall - walls[i]
    return rain
