from random import choice, randint

from brain_games.types import Round

MIN = -10
MAX = 10
SIGNS = ["+", "-", "*"]
DESCRIPTION = "What is the result of the expression?"


def get_correct_answer(operands: tuple[int, int], sign: str) -> str:
    match sign:
        case "+":
            return str(operands[0] + operands[1])
        case "-":
            return str(operands[0] - operands[1])
        case "*":
            return str(operands[0] * operands[1])
        case _:
            raise ValueError(f"Unexpected sign: {sign}")


def get_round() -> Round:
    operands = (randint(MIN, MAX), randint(MIN, MAX))  # NOSONAR
    sign = choice(SIGNS)  # NOSONAR

    return {
        "question": f"{operands[0]} {sign} {operands[1]}",
        "answer": get_correct_answer(operands, sign),
    }
