from brain_games.random import randint
from brain_games.types import Round

MIN = 1
MAX = 100


def get_correct_answer(a: int, b: int) -> str:
    while b != 0:
        a, b = b, a % b

    return str(a)


DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_round() -> Round:
    operands = [randint(MIN, MAX), randint(MIN, MAX)]

    return {
        "question": f"{operands[0]} {operands[1]}",
        "answer": get_correct_answer(*sorted(operands)),
    }
