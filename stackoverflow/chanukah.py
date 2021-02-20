#!/bin/python3
import sys

lines = sys.stdin.readlines()[1:]

for line in lines:
    params = line.split()
    params[1] = int(params[1])

    n = 0
    for i in range(0, params[1]+1):
        n += i + 1

    print(params[0], n-1)
