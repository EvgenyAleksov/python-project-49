from brain_games.greeting import greeting
from brain_games.answer import answer


def main():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    answer(name, 'gcd')
