from brain_games.tasks.calc import calculate
from brain_games.engine import engine


def main():
    rule = 'What is the result of the expression?'
    engine(rule, calculate)
