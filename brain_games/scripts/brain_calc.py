from brain_games.games.calc import calculate
from brain_games.games.calc import set_task
from brain_games.engine import play


def main():
    play(set_task, calculate)
