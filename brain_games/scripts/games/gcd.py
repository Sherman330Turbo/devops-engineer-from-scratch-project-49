from collections.abc import Callable

from brain_games.random import randint
from brain_games.types import GetRound, Round


def get_correct_answer(a: int, b: int) -> str:
    while b != 0:
        a, b = b, a % b

    return str(a)


def get_round_generator() -> GetRound:
    def get_round() -> Round:
        operands = [randint(1, 100), randint(1, 100)]

        return {
            "question": f"{operands[0]} {operands[1]}",
            "answer": get_correct_answer(*sorted(operands)),
        }

    return get_round


def gcd_game() -> tuple[str, Callable[[], GetRound]]:
    return (
        "Find the greatest common divisor of given numbers.",
        get_round_generator,
    )
