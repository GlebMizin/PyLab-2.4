#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    il = list(map(int, input().split()))
    if len(il) != 10:
        print("Wrong list range", file=sys.stderr)
        exit(1)

    ol = [num for ind, num in enumerate(il) if num % 3 == 0 and num != 0]
    il = [ind for ind, num in enumerate(il) if num % 3 == 0 and num != 0]

    print(f'List of all elements divisible by three: {ol}')
    print(f'Index of last element divisible by three: {il[-1]}')
