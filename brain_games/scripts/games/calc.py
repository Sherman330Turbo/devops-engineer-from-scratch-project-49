import random
from collections.abc import Callable

from brain_games.types import GetRound


def get_random_number(begin: int, end: int) -> int:
    return random.randint(begin, end)  # NOSONAR - not security-sensitive


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
            shuffled_sign = random.sample(
                signs, k=len(signs)
            )  # NOSONAR - not security-sensitive
        return shuffled_sign.pop()

    return get_new_sign


def get_round_generator() -> GetRound:
    get_sign = get_sign_generator()

    def get_round():
        operands = (get_random_number(-10, 10), get_random_number(-10, 10))
        sign = get_sign()

        question = f"{operands[0]} {sign} {operands[1]}"
        answer = get_correct_answer(operands, sign)
        return {"question": question, "answer": answer}

    return get_round


def calc_game() -> tuple[str, Callable[[], GetRound]]:
    return (
        "What is the result of the expression?",
        get_round_generator,
    )
