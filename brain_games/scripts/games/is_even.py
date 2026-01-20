import random
from collections.abc import Callable

from brain_games.types import GetRound


def get_random_number(begin: int, end: int) -> int:
    return random.randint(begin, end)  # NOSONAR - not security-sensitive;


def get_correct_answer(question: int) -> str:
    return "yes" if question % 2 == 0 else "no"


def get_round_generator() -> GetRound:
    def get_round() -> dict[str, str]:
        question = get_random_number(1, 100)
        answer = get_correct_answer(question)
        return {"question": question, "answer": answer}

    return get_round


def is_even_game() -> tuple[str, Callable[[], GetRound]]:
    return (
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_round_generator,
    )
