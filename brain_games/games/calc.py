import random
from random import choice
import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculate():
    rule = 'What is the result of the expression?'
    sign = ['+', '-', '*']
    x = random.randrange(0, 100)
    y = random.randrange(0, 100)
    op = choice(sign)
    return rule, f'{x} {op} {y}', str(OPERATORS[op](x, y))
