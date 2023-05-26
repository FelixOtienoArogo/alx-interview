#!/usr/bin/python3
""" N queens """
import sys


n = sys.argv[1]

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not n.isdigit():
    print("N must be a number")
    exit(1)

n = int(n)

if n < 4:
    print("N must be at least 4")
    exit(1)


def pos_queens(n, num=0, first=[], sec=[], third=[]):
    """ find possible positions """
    if num < n:
        for i in range(n):
            if i not in first and num + i not in sec and num - i not in third:
                yield from pos_queens(n, num + 1, first + [i],
                                      sec + [num + i], third + [num - i])
    else:
        yield first


def sol(n):
    """ solve """
    fin = []
    i = 0
    for ans in pos_queens(n, 0):
        for a in ans:
            fin.append([i, a])
            i += 1
        print(fin)
        fin = []
        i = 0


sol(n)
