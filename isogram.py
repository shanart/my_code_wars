"""
https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
"""


def is_isogram(string) -> bool:
    letters = []
    for letter in list(string.lower()):
        if letter in letters:
            return False
        letters.append(letter)
    return True


"""
This is my solution)) Based on creating the list of unrepeatable elements. If 
next letter is already in the list - given string is not isogram.

====
But smarter solution will be by using set(). Set in python is a data structure
with non repitable elements in it. So by transforming given string in to set:
```
set(string.lower())
```
we will have a list of unique letters in string. Then we can compare it
with the given string:
```
len(string) == len(set(string.lower()))
```
And if they not equal - the string has repitable elements in it, wich means that
the given string is not isogram. Very simple brilliant solution based on knowing
python data structures
"""

if __name__ == "__main__":
    print(is_isogram("Dermatoglyphics"))
    # True
    print(is_isogram("isogram"))
    # True
    print(is_isogram("aba"))
    # False, "same chars may not be adjacent"
    print(is_isogram("moOse"))
    # False, "same chars may not be same case"
    print(is_isogram("isIsogram"))
    # False
    print(is_isogram(""))
    # True, "an empty string is a valid isogram"
