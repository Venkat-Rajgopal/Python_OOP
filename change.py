# Uses python3
import sys

def get_change(m):
    #write your code here
    large = 10
    mid = 5
    small = 1
    result = 0

    coins = [large, mid, small]

    while m != 0:
        for coin in coins:
            if (m - coin >= 0):
                m -= coin
                print(m)
                result = result + 1
                break

    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
