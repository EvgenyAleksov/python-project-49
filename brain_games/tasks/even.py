import random


def calculate():
    random_number = random.randrange(0, 400)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, correct_answer
