#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    output_list = []
    arr = sorted(arr)
    minimum_difference = 10 ** 18
    for i in range(1, len(arr)):
        absolute_difference = abs(arr[i - 1] - arr[i])

        if absolute_difference < minimum_difference:
            output_list = [(arr[i - 1], arr[i])]
            minimum_difference = absolute_difference

        elif absolute_difference == minimum_difference:
            output_list.append((arr[i - 1], arr[i]))

    closest = [i for listed in output_list for i in listed]
    return closest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
