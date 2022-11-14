#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    inp_list = list(map(int, input().split()))
    out_list = list()
    if len(inp_list) != 10:
        print("Wrong list range", file=sys.stderr)
        exit(1)

    for ind, num in enumerate(inp_list):
        if num % 3 == 0 and num != 0:
            out_list.append(num)
            last_index = ind + 1
    print(out_list)
    print(last_index)

    print(f'List of all elements divisible by three: {out_list}')
    print(f'Index of last element divisible by three: {last_index}')
