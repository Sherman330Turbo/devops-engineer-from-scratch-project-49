from collections.abc import Callable

from brain_games.random import randint
from brain_games.types import GetRound, Round

RANGE = 10


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


def get_round_generator() -> GetRound:
    def get_round() -> Round:
        base = randint(0, 5)
        delta = randint(2, 9)
        progression = [base + (delta * idx) for idx in range(RANGE)]
        hidden_index = randint(0, RANGE - 1)

        return {
            "question": get_question(progression, hidden_index),
            "answer": str(progression[hidden_index]),
        }

    return get_round


def progression_game() -> tuple[str, Callable[[], GetRound]]:
    return (
        "What number is missing in the progression?",
        get_round_generator,
    )
