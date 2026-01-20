import random


def get_random_number(begin: int, end: int) -> int:
    return random.randint(begin, end)  # NOSONAR - not security-sensitive;


def get_correct_answer(question: int) -> str:
    return "yes" if question % 2 == 0 else "no"


def get_round():
    question = get_random_number(1, 100)
    answer = get_correct_answer(question)
    return {"question": question, "answer": answer}


def is_even_game():
    return (
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_round,
    )
