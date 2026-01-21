from collections.abc import Callable

from brain_games.random import randint, sample
from brain_games.types import GetRound, Round

MIN = -10
MAX = 10


def get_correct_answer(operands, sign) -> str:
    match sign:
        case "+":
            return str(operands[0] + operands[1])
        case "-":
            return str(operands[0] - operands[1])
        case "*":
            return str(operands[0] * operands[1])
        case _:
            raise ValueError(f"Unexpected sign: {sign}")


def get_sign_generator() -> Callable[[], str]:
    signs = ["+", "-", "*"]
    shuffled_sign: list[str] = []

    def get_new_sign() -> str:
        nonlocal shuffled_sign
        if len(shuffled_sign) == 0:
            shuffled_sign = sample(signs, k=len(signs))
        return shuffled_sign.pop()

    return get_new_sign


def get_round_generator() -> GetRound:
    get_sign = get_sign_generator()

    def get_round() -> Round:
        operands = (randint(MIN, MAX), randint(MIN, MAX))
        sign = get_sign()

        return {
            "question": f"{operands[0]} {sign} {operands[1]}",
            "answer": get_correct_answer(operands, sign),
        }

    return get_round


def calc_game() -> tuple[str, Callable[[], GetRound]]:
    return (
        "What is the result of the expression?",
        get_round_generator,
    )
