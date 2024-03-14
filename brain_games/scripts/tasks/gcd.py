import random


def task():
    x = random.randrange(2, 100)
    y = random.randrange(2, 100)
    print('Question: ', x, y)

    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    return str(x)
