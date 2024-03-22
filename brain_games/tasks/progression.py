import random


def calculate():
    begin = random.randrange(1, 30)
    step = random.randrange(1, 20)
    length = random.randrange(5, 12)
    end = begin + step * length

    progr = []
    for i in range(begin, end, step):
        progr.append(i)

    x = random.randrange(0, length)
    hide = progr[x]
    progr[x] = '..'
    res = ''
    for i in progr:
        res = res + str(i) + ' '

    print('Question:', res)
    return str(hide)
