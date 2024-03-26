from brain_games.games.progression import calculate
from brain_games.engine import play


def main():
    rule = 'What number is missing in the progression?'
    play(rule, calculate)
