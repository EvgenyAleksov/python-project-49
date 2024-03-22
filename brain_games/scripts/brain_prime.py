from brain_games.tasks.prime import calculate
from brain_games.engine import engine


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(rule, calculate)
