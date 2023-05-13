#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re


def printstat(code: dic, size: int) -> None:
    """
    helper function
    """
    print(f"File size: {size}")
    for i in sorted(code.keys()):
        if code[i] != 0:
            print(f"{i}: {code[i]}")


line_reg = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[(.+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$')
count = 0
size = 0
codes = {"200": 0,
         "301": 0,
         "400": 0,
         "401": 0,
         "403": 0,
         "404": 0,
         "405": 0,
         "500": 0}
try:
    for line in sys.stdin:
        line = line.strip()
        count += 1
        try:
            size += int(line[-1])
        except Exception:
            pass

        if line_reg.match(line):
            lis = line.split()
            count += 1
            try:
                size += int(line[-1])
            except Exception:
                pass
            try:
                if lis[-2] in codes:
                    codes[lis[-2]] += 1
            except Exception:
                pass
            if count % 10 == 0:
                printstat(codes, size)

except KeyboardInterrupt:
    printstat(codes, size)
    raise
