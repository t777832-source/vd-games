from VD_games.engine import run_game
from VD_games.games.progression_game import (
    DESCRIPTION,
    get_question_and_answer,
)


def main():
    run_game(DESCRIPTION, get_question_and_answer)
