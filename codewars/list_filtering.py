'''
Create a function that takes a list of non-negative integers and strings as inputs and returns a new list with string filtered out. 

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''


def filter_list(l):
    new_list = []
    for i in l:
        if type(i) == int:
            new_list.append(i)
    
    print(new_list)
    return(new_list)



filter_list([1,2,'aasf','1','123',123])
