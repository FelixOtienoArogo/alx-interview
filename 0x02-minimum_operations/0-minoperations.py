#!/usr/bin/python3

'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n: int) -> int:
    '''
    returns min operations to get n Hs
    '''
    i: int = 1
    op: int = 0
    temp: int = i
    while i < n:
        if i == 1:
            op += 2
            i += 1
        elif (n % i) == 0:
            temp = i
            i = i * 2
            op += 2
        else:
            i = i + temp
            op += 1
    if i == n:
        return op
    return 0
