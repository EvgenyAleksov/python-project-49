from brain_games.tasks.even import calculate
from brain_games.engine import engine


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine(rule, calculate)
