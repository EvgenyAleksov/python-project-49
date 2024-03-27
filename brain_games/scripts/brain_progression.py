#!/usr/bin/env python3

from brain_games.games.progression import calculate
from brain_games.games.progression import set_task
from brain_games.engine import play


def main():
    play(set_task, calculate)


if __name__ == '__main__':
    main()
