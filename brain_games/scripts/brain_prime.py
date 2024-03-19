from brain_games.greeting import greeting
from brain_games.scripts.tasks.prime import task
from brain_games.answer import answer


def main():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(1, 4):
        if answer(name, task()) is False:
            break
        elif i == 3:
            print('Congratulations, ' + name + '!')
