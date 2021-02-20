#!/bin/python3
import sys
_ = input()
for line in sys.stdin:
    print(len(str(int(line))))
