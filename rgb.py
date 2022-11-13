"""
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""
def rgb(r, g, b):
    res = ''
    for i in list(map(lambda x: 255 if x > 255 else (0 if x < 0 else x), [r, g, b])):
        res += f"0{i:X}" if len(f"{i:X}") < 2 else f"{i:X}"
    return res


# Even more ridiculous list comprehensions :)
def rgb_unreadable(r, g, b):
    return "".join([f"0{i:X}" if len(f"{i:X}") < 2 else f"{i:X}" for i in list(map(lambda x: 255 if x > 255 else (0 if x < 0 else x), [r, g, b]))])


"""
The human readable solutions are here:
https://www.codewars.com/kata/513e08acc600c94f01000001/solutions/python

"""

if __name__ == "__main__":
    print(rgb(0, 0, 0))
    print(rgb(1, 2, 3))
    print(rgb(255, 255, 255))
    print(rgb(254, 253, 252))
    print(rgb(-20, 275, 125))