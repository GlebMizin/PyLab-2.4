#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    inp_list = list(map(int, input().split()))
    out_list = list()
    if len(inp_list) != 10:
        print("Wrong list range", file=sys.stderr)
        exit(1)

    ind_list, out_list = zip(*[(ind + 1, num) for ind, num in enumerate(inp_list) if num % 3 == 0 and num != 0])

    print(f'List of all elements divisible by three: {out_list}')
    print(f'Index of last element divisible by three: {ind_list[-1]}')
