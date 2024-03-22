from brain_games.tasks.gcd import calculate
from brain_games.engine import engine


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    engine(rule, calculate)
