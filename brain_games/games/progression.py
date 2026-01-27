from random import randint

from brain_games.types import Round

RANGE = 10
BASE_MIN = 0
BASE_MAX = 5
DELTA_MIN = 1
DELTA_MAX = 100
DESCRIPTION = "What number is missing in the progression?"


def get_question(progression: list[int], hidden_index: int) -> str:
    result = ""
    for idx in range(len(progression)):
        if len(result) != 0:
            result += " "
        if idx == hidden_index:
            result += ".."
        else:
            result += str(progression[idx])

    return result


def get_round() -> Round:
    base = randint(BASE_MIN, BASE_MAX)  # NOSONAR
    delta = randint(DELTA_MIN, DELTA_MAX)  # NOSONAR
    progression = [base + (delta * idx) for idx in range(RANGE)]
    hidden_index = randint(0, RANGE - 1)  # NOSONAR

    return {
        "question": get_question(progression, hidden_index),
        "answer": str(progression[hidden_index]),
    }
