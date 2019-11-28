# -> is a function annotation
# http://www.python.org/dev/peps/pep-3107/

# Check the word for a palindrome
def isPalindrome(word: str) -> bool:

    if(word == word[::-1]): # reverse the word and check
        return True
    return False

def getPalindromes(inputStr: str) -> list:

    # clean the input string and split the srings to words
    cleanStr = inputStr.replace(",","").lower()
    words = set(cleanStr.split(" "))

    # Iterate through each word and use list comprehension
    wPalindromes = [
        word for word in words 
        if isPalindrome(word) and word != ""
    ]
    return wPalindromes

getPalindromes('Lol, hah This is a joke')