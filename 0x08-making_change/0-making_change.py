#!/usr/bin/python3
"""A function that will determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """
    this is the function to determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
