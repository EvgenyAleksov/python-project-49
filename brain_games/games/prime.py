import random


def find_prime(x):
    correct_answer = 'yes'
    i = 2
    while i <= int(x / 2):
        if x % i == 0:
            correct_answer = 'no'
        i = i + 1
    return correct_answer


def calculate():
    x = random.randrange(2, 100)
    return x, find_prime(x)
