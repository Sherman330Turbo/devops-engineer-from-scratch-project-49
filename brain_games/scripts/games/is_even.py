from collections.abc import Callable

from brain_games.random import randint
from brain_games.types import GetRound, Round


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round_generator() -> GetRound:
    def get_round() -> Round:
        question = randint(1, 100)
        return {
            "question": str(question),
            "answer": "yes" if is_even(question) else "no",
        }

    return get_round


def is_even_game() -> tuple[str, Callable[[], GetRound]]:
    return (
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_round_generator,
    )
