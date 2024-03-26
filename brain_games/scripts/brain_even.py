from brain_games.games.even import calculate
from brain_games.engine import play


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    play(rule, calculate)
