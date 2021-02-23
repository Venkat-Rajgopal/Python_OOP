#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob   = 0

    for i in range(3):
        # if both are same then no points are assigned. 

        if a[i]>b[i] :
            alice += 1

        elif a[i]<b[i]:
            bob+=1

    print(f'Alice score is {alice} and Bob\'s score {bob}')
    return alice, bob        


compareTriplets(a=[10,20,30], b=[5,5,50])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
