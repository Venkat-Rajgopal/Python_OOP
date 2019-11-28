# replicate the sum of any number of variables
# note how arguments can be used

def sum(*args):

    # initiate a val
    val = 0
    
    # add the args 
    for arg in args:
        val += arg
    
    return val

sum(1,2)