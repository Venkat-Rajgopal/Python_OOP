# Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

# monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# monkeyCount(1) # --> [1]

def monkey_count(n):
    count = []
    for i in range(n+1):
        count.append(i)    
    count = count[1:n+1]
    return count
monkey_count(5)


# An elegant solution
def monkey_count_(n):
    return list(range(1,n+1))
monkey_count_(5)