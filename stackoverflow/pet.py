#!/bin/python3
import sys
n = 1
maxpoints = -1
maxn = -1

for line in sys.stdin:
    points = sum([int(w) for w in line.split()])
    if points > maxpoints:
        maxpoints = points
        maxn = n
    if n == 5:
        break
    n += 1

print(n-1, maxpoints)
