from brain_games.greeting import greeting
from brain_games.scripts.tasks.progression import task
from brain_games.answer import answer


def main():
    name = greeting()
    print('What number is missing in the progression?')

    for i in range(1, 4):
        if answer(name, task()) is False:
            break
        elif i == 3:
            print('Congratulations, ' + name + '!')
