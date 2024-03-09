import random


def even_num():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()

    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    answer = ''
    stage = 1
    while stage <= 3:
        random_number = random.randrange(0, 400)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'

        print('Question: ', random_number)
        answer = input()
        print('Your answer: ' + answer)

        if answer == correct_answer:
            print('Correct!')
            if stage == 3:
                print('Congratulations, ' + name + '!')
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '"
                  + correct_answer + "'.\nLet's try again, " + name + "!")
            break

        stage = stage + 1
