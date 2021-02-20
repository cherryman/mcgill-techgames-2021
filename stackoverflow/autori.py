#!/bin/python3
line = input()
print(''.join([word[0] for word in line.split('-')]))
