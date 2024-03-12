import random


def greetings():
    global name
    name = ''
    print('Welcome to the Brain Games!')
    while name == '':
        print('May I have your name? ', end='')
        name = input()

    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')


def task():
    global correct_answer
    x = random.randrange(2, 100)
    y = random.randrange(2, 100)
    print('Question: ', x, y)

    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    correct_answer = x


def gcd():
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
