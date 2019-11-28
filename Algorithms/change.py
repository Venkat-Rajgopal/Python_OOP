# Uses python3
import sys

""" Find the minimum number of coins needed 
    to change the input value into coins with denominations
    1, 5, 10 
"""

def get_change(m):

    large = 10
    mid = 5
    small = 1
    result = 0

    coins = [large, mid, small]

    while m != 0:
        for coin in coins:
            if (m - coin >= 0):
                m -= coin
                result = result + 1
                break

    return result

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
