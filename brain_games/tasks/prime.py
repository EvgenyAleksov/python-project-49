import random


def calculate():
    x = random.randrange(2, 100)
    print(x)

    correct_answer = 'yes'
    i = 2
    while i <= int(x / 2):
        if x % i == 0:
            correct_answer = 'no'
        i = i + 1

    print('Question:', x)
    return correct_answer
