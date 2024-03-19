def answer(name, task):
    correct_answer = task
    my_answer = input()
    print('Your answer: ', my_answer)

    if my_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("'" + my_answer + "' is wrong answer ;(. Correct answer was '"
              + str(correct_answer) + "'.\nLet's try again, " + name + "!")
        return False
