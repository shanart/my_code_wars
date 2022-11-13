"""
https://www.codewars.com/kata/54599705cbae2aa60b0011a4/python
"""


def one(sq, fun):
    return len(list(filter(fun, sq))) == 1


if __name__ == "__main__":
    equals_9 = lambda x: x == 9
    less_than_9 = lambda x: x < 9
    greater_than_9 = lambda x: x > 9
    arr = (6, 7, 8, 9, 10, 11)

    print(one(arr, equals_9))
    print(one(arr, less_than_9))
    print(one(arr, greater_than_9))
