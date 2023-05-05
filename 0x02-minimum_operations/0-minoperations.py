#!/usr/bin/python3

'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n):
    '''
    returns min operations to get n Hs
    '''
    op = 0
    idx = 2
    if n < 2:
        return 0
    while (idx < n + 1):
        while n % idx == 0:
            op += idx
            n /= idx
        idx += 1
    return op
