from brain_games.greeting import greeting
from brain_games.answer import answer


def main():
    name = greeting()
    print('What is the result of the expression?')
    answer(name, 'calc')
