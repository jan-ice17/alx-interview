#!/usr/bin/python3

"""
This script reads lines from standard input, tracking the total file size 
and counts of specific HTTP status codes, and outputs metrics every 10 lines.
"""

import sys

def print_stats(dic, size):
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))

sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_stats(sts, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in sts:
                sts[stlist[-2]] += 1
        except:
            pass
    print_stats(sts, size)

except KeyboardInterrupt:
    print_stats(sts, size)
    raise
