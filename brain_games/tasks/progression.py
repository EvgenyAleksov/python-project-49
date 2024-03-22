import random


def gen_progr():
    begin = random.randrange(1, 30)
    step = random.randrange(1, 20)
    global length
    length = random.randrange(5, 12)
    end = begin + step * length

    global progr
    progr = []
    for i in range(begin, end, step):
        progr.append(i)

    return length, progr


def calculate():
    gen_progr()
    x = random.randrange(0, length)
    hide = progr[x]
    progr[x] = '..'
    res = ''
    for i in progr:
        res = res + str(i) + ' '

    print('Question:', res)
    return str(hide)
