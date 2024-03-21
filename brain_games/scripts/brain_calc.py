from brain_games.greeting import greeting
from brain_games.scripts.tasks.calc import task
from brain_games.answer import answer


def main():
    name = greeting()
    print('What is the result of the expression?')

    for i in range(1, 4):
        if answer(name, task()) is False:
            break
        elif i == 3:
            print(f'Congratulations, {name}!')
