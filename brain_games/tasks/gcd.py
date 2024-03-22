import random


def find_gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return str(x)


def calculate():
    x = random.randrange(2, 100)
    y = random.randrange(2, 100)
    print('Question:', x, y)
    return find_gcd(x, y)
