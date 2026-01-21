import math
from collections.abc import Callable

from brain_games.random import randint
from brain_games.types import GetRound, Round

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


def get_round_generator() -> GetRound:
    def get_round() -> Round:
        target = randint(MIN, MAX)

        return {
            "question": str(target),
            "answer": "yes" if is_prime(target) else "no",
        }

    return get_round


def is_prime_game() -> tuple[str, Callable[[], GetRound]]:
    return (
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        get_round_generator,
    )
