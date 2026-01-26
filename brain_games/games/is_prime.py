import math

from brain_games.random import randint
from brain_games.types import Round

MIN = 1
MAX = 100


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    target = math.isqrt(number)
    for idx in range(3, target + 1, 2):
        if number % idx == 0:
            return False

    return True


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round() -> Round:
    target = randint(MIN, MAX)

    return {
        "question": str(target),
        "answer": "yes" if is_prime(target) else "no",
    }
