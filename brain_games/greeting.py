def greeting():
    name = ''
    print('Welcome to the Brain Games!')
    while name == '':
        print('May I have your name? ', end='')
        name = input()

    print(f'Hello, {name}!')
    return name
