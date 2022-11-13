"""
https://www.codewars.com/kata/546dba39fa8da224e8000467/train/python
"""

def run_length_encoding(s) -> list:
    if not s: return []
    result = []
    for i, l in enumerate(s):
        if l != s[i-1] or not result:
            result.append([1, l])
        else:
            result[-1][0] += 1
    return result

"""
But much clever implementation on codewars was by using intertools.groupby() with list comprehensions
```
from itertools import groupby
def run_length_encoding(s) -> list:
    return [[sum(1 for _ in g), c] for c, g in groupby(s)]
```
Well... you need to know the standard library well to make smart decisions instead of reinventing the 
wheel in simple situations
"""


if __name__ == "__main__":
    print(run_length_encoding(''))
    print(run_length_encoding("abc"))
    print(run_length_encoding("aaaaab"))
    print(run_length_encoding("hello world!"))
    print(run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb"))
    print(run_length_encoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"))
