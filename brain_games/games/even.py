import random


def set_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate():
    random_number = random.randrange(0, 400)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, correct_answer
