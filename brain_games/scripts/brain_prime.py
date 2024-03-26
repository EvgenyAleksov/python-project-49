from brain_games.games.prime import calculate
from brain_games.engine import play


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play(rule, calculate)
