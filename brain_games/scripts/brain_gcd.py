from brain_games.games.gcd import calculate
from brain_games.engine import play


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    play(rule, calculate)
