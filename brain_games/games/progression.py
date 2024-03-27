import random


def gen_progr():
    begin = random.randrange(1, 20)
    step = random.randrange(1, 20)
    length = random.randrange(5, 12)
    end = begin + step * length
    progr = []
    for i in range(begin, end, step):
        progr.append(i)
    return progr


def calculate():
    rule = 'What number is missing in the progression?'
    progr = gen_progr()
    x = random.randrange(0, len(gen_progr()))
    hide = progr[x]
    progr[x] = '..'
    res = ''
    for i in progr:
        res = res + str(i) + ' '
    return rule, res, str(hide)
