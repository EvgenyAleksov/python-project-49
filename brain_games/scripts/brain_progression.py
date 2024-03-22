from brain_games.tasks.progression import calculate
from brain_games.engine import engine


def main():
    rule = 'What number is missing in the progression?'
    engine(rule, calculate)
