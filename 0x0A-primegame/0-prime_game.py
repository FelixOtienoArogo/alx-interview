#!/usr/bin/python3
"""Function isWinner."""


def isPrime(n):
    """Determine that a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Return name of the player that won the most rounds."""
    winner = "Maria"
    Maria = 0
    Ben = 0
    if not nums or x < 1:
        return None
    for n in nums:
        numbers = list(range(1, n + 1, 1))

        i = 0
        play = 0
        ben_win = 0
        maria_win = 0
        while(len(numbers) >= 1 and i < len(numbers)):
            play += 1
            if isPrime(numbers[i]):
                for j in numbers:
                    if j % numbers[i] == 0:
                        numbers.remove(j)
                        i = 0
            if play % 2 == 0:
                maria_win = 1
                ben_win = 0
            else:
                ben_win = 1
                maria_win = 0
            i += 1
        Ben += ben_win
        Maria += maria_win
    if(Ben < Maria):
        winner = "Maria"
    elif(Ben > Maria):
        winner = "Ben"
    else:
        winner = None
    return winner
