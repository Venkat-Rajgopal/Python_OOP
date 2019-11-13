# Given an integral number, determine if it's a square number:

def is_square(n):    
    res = n >= 0  and (n**.5).is_integer()
    return res


    