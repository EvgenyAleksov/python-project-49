from brain_games.games.calc import calculate
from brain_games.engine import play


def main():
    rule = 'What is the result of the expression?'
    play(rule, calculate)
