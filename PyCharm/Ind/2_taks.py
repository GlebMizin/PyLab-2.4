#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    inp_list = list(map(float, input().split()))
    final_out = list()
    prod = 1
    Sum = 0

    # Multiply all non-negative elements
    for item in inp_list:
        if item > 0:
            prod *= item

    # Sum all the elements until we meet the minimum
    for item in inp_list:
        if item > min(inp_list):
            Sum += item
        else:
            break

    # Split the initial list into two, with even and odd elements
    f_out = inp_list[::2]
    s_out = inp_list[1::2]

    # Sort new lists
    f_out.sort()
    s_out.sort()

    # Create a new list by inserting elements one by one from the sorted lists
    for i, v in enumerate(f_out):
        if i == len(s_out):
            final_out.append(f_out[i])
            break
        else:
            final_out.append(f_out[i])
            final_out.append(s_out[i])

    # Output
    print(f'Product of non-negative numbers: {prod}')
    print(f'The sum of the elements before meeting the minimum: {Sum}')
    print(f'List sorted according to task condition: {final_out}')
