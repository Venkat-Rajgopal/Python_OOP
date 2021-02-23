# 
import math
import os


def arr_sum(ar):
    summe = 0;
    for i in range(len(ar)):
        print(i)
        summe += ar[i]
    return summe

print(arr_sum(ar = [1,2,3]))
