# given an input string return the person who likes
# Example
# Function takes an input array, containing names ('Strings') of people who like an item
# Return: Text as '[Name] likes this'


def likes(names):
    
    return_text = ''

    if  (len(names) == 0):
        return_text = 'no one likes this'

    elif (len(names) == 1):
        return_text = str(names[0]) + ' ' + 'likes this'

    elif (len(names) == 2):
        return_text = str(names[0]) + ' ' + 'and' + ' ' + str(names[1]) + ' ' + 'like this'

    elif (len(names) == 3):
        return_text = str(names[0]) + ', ' +  str(names[1]) + ' ' + 'and' + ' ' + str(names[2]) + ' ' + 'like this'

    elif (len(names) > 3):
        return_text = str(names[0])  + ', ' + str(names[1]) + ' ' + 'and' + ' ' + str(len(names)-2) + ' ' + 'others like this'


    print(return_text)

    return return_text

names = ['Peter', 'Pan', 'Cake', 'Pizza']
likes(names)


# Alternative solution
# elegant solution
def likes_(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


names = ['Peter', 'Cake']
print(likes_(names))