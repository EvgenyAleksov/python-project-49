#!/usr/bin/env python3

from brain_games.games.calc import set_task, calculate
from brain_games.engine import play


def play_calc():
    play(set_task, calculate)


if __name__ == '__main__':
    play_calc()
