def answer(name, task):
    if task == 'even':
        from brain_games.scripts.tasks.even import task
    if task == 'calc':
        from brain_games.scripts.tasks.calc import task
    if task == 'even':
        from brain_games.scripts.tasks.gcd import task
    if task == 'progression':
        from brain_games.scripts.tasks.progression import task

    stage = 1
    while stage <= 3:
        correct_answer = task()
        answer = input()
        print('Your answer: ' + answer)

        if answer == correct_answer:
            print('Correct!')
            if stage == 3:
                print('Congratulations, ' + name + '!')
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '"
                  + str(correct_answer) + "'.\nLet's try again, " + name + "!")
            break

        stage = stage + 1
