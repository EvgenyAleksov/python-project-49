import random
from random import choice
import operator


def get_op(op):
    get_op = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }.get
    return get_op(op)


def calculate():
    sign = ['+', '-', '*']
    x = random.randrange(0, 100)
    y = random.randrange(0, 100)
    op = choice(sign)
    return f'{x} {op} {y}', str(get_op(op)(x, y))
