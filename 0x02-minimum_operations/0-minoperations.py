#!/usr/bin/python3

"""
Determines the minimum number of operations required to achieve exactly n 'H' characters.
"""

def minOperations(n):
    """
    Calculates the fewest operations needed to reach exactly n 'H' characters.

    Args:
        n (int): Target number of 'H' characters.

    Returns:
        int: Minimum number of operations needed.
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
