from brain_games.greeting import greeting
from brain_games.answer import answer


def main():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer(name, 'even')
