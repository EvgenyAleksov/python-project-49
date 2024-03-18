from brain_games.greeting import greeting
from brain_games.answer import answer


def main():
    name = greeting()
    print('What number is missing in the progression?')
    answer(name, 'progression')
