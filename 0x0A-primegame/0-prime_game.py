#!/usr/bin/python3
"""Function isWinner."""


def isWinner(x, nums):
    """Return the player who won the most rounds."""
    if not nums or x < 1:
        return None
    maximum = max(nums)
    winner = "Ben"
    sort = [True for _ in range(max(maximum + 1, 2))]
    for i in range(2, int(maximum ** 0.5) + 1):
        if not sort[i]:
            continue
        for j in range(i*i, maximum + 1, i):
            sort[j] = False

    sort[0] = sort[1] = False
    c = 0
    for i in range(len(sort)):
        if sort[i]:
            c += 1
        sort[i] = c

    maria_win = 0
    for n in nums:
        maria_win += sort[n] % 2 == 1
    if maria_win * 2 == len(nums):
        winner = None
    if maria_win * 2 > len(nums):
        winner = "Maria"
    return winner
