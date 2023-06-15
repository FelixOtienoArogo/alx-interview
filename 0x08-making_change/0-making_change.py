#!/usr/bin/python3
"""Change comes from within."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    check = 0
    comp = total

    for coin in coins:
        if int(total / coin) > 0:
            div = int(total / coin)
            check += (div * coin)
            count += int(total / coin)
        total = total % coin
    if check == comp:
        return count
    return -1
