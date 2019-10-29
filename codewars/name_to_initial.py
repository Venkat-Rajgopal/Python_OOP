""" Function to convert a name into initials. Strictly takes two words with one space in between them.
The output should be two capital letters with a dot seperating them.
Example
Sam Harris => S.H
Patrick Feeney => P.F
"""

def abbrevName(name):
    
    splits = name.split()
    
    # split word into characters. 
    def split(word): 
        return [char for char in word] 
    
    abbr = split(splits[0])[0].upper() + '.' + split(splits[1])[0].upper()
    
    return abbr



# Alternative solutions using list comprehension
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


abbrevName(name = 'Sam harris')