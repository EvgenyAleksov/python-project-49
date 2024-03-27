import prompt
from brain_games.greeting import greeting
STAGES = 3


def play(calculate):
    name = greeting()
    rule = calculate()[0]
    print(rule)

    for i in range(1, STAGES + 1):
        quest, correct_answer = calculate()[1:]
        print('Question:', quest)
        my_answer = prompt.string('')
        print('Your answer:', my_answer)

        if my_answer == correct_answer:
            print('Correct!')
            if i == STAGES:
                print(f'Congratulations, {name}!')
        else:
            print(f"""'{my_answer}' is wrong answer ;(. \
Correct answer was '{str(correct_answer)}'.
Let's try again, {name}!""")
            break
