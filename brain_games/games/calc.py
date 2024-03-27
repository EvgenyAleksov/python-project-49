import random
from random import choice
import operator


def set_task():
    return 'What is the result of the expression?'


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculate():
    sign = ['+', '-', '*']
    x = random.randrange(0, 100)
    y = random.randrange(0, 100)
    op = choice(sign)
    return f'{x} {op} {y}', str(OPERATORS[op](x, y))
