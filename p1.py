#!/usr/bin/env python3

import sys
import itertools
ls = [l.strip() for l in sys.stdin.readlines()]

for [a, b] in itertools.combinations(ls, 2):
    if int(a) + int(b) == 2020:
        print(int(a)*int(b))
        break
