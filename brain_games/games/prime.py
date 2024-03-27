import random


def is_prime(x):
    correct_answer = True
    i = 2
    while i <= int(x / 2):
        if x % i == 0:
            correct_answer = False
        i = i + 1
    return correct_answer


def calculate():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    x = random.randrange(2, 100)
    return rule, x, 'yes' if is_prime(x) is True else 'no'
