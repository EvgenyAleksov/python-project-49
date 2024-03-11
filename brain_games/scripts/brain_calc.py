import random
from random import choice


def greetings():
    global name
    name = ''
    print('Welcome to the Brain Games!')
    while name == '':
        print('May I have your name? ', end='')
        name = input()

    print('Hello, ' + name + '!')
    print('What is the result of the expression?')


def task():
    global correct_answer
    sign = ['+', '-', '*']
    x = random.randrange(0, 100)
    y = random.randrange(0, 100)
    op = choice(sign)

    if op == '+':
        correct_answer = x + y
    elif op == '-':
        correct_answer = x - y
    else:
        correct_answer = x * y

    print('Question: ', x, op, y)


def calc_oper():
    global answer
    greetings()

    stage = 1
    while stage <= 3:
        task()

        answer = input()
        print('Your answer: ' + answer)

        if int(answer) == correct_answer:
            print('Correct!')
            if stage == 3:
                print('Congratulations, ' + name + '!')
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '"
                  + str(correct_answer) + "'.\nLet's try again, " + name + "!")
            break

        stage = stage + 1
