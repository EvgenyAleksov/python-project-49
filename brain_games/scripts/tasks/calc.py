import random
from random import choice


def task():
    sign = ['+', '-', '*']
    x = random.randrange(0, 100)
    y = random.randrange(0, 100)
    op = choice(sign)

    if op == '+':
        correct_answer = x + y
    elif op == '-':
        correct_answer = x - y
    else:
        correct_answer = x * y

    print('Question: ', x, op, y)
    return str(correct_answer)
