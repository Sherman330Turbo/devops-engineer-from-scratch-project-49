import math
from collections.abc import Callable

from brain_games.random import randint
from brain_games.types import GetRound, Round


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True

    target = math.isqrt(number)
    for idx in range(3, target + 1, 2):
        if number % idx == 0:
            return False

    return True


def get_round_generator() -> GetRound:
    def get_round() -> Round:
        target = randint(1, 50)

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
