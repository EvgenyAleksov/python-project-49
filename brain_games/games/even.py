import random


def calculate():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_number = random.randrange(0, 400)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return rule, random_number, correct_answer
