#!/bin/python3
import sys
from collections import Counter
if __name__ == "__main__":
    s = input().strip()
    counts = sorted(
    sorted(Counter(s).items(), key=lambda x: x[0]),
    key=lambda y: y[1], reverse=True)
    for char, count in counts[:3]:
        print(char, count)