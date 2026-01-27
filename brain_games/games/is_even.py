from random import randint

from brain_games.types import Round

MIN = 1
MAX = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round() -> Round:
    question = randint(MIN, MAX)  # NOSONAR
    return {
        "question": str(question),
        "answer": "yes" if is_even(question) else "no",
    }
