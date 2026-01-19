import random

import prompt

from brain_games.cli import congrats_user, get_user_name, welcome_user

ROUNDS = 3
YES_ANSWER = "yes"
NO_ANSWER = "no"


def get_random_number(begin: int, end: int) -> int:
    return random.randint(begin, end)


def get_correct_answer(question: int) -> str:
    return YES_ANSWER if question % 2 == 0 else NO_ANSWER


def game() -> None:
    print("Welcome to the Brain Games!")

    user_name = get_user_name()
    welcome_user(user_name)
    print(
        f'Answer "{YES_ANSWER}" if the number is even, '
        f'otherwise answer "{NO_ANSWER}".'
    )
    correct_answers = 0
    while correct_answers < ROUNDS:
        question = get_random_number(1, 100)
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(question)

        if answer == correct_answer:
            correct_answers += 1
            print("Correct!")
        else:
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {correct_answer}."
            )
            print(f"Let's try again, {user_name}!")
            break

    if correct_answers == ROUNDS:
        congrats_user(user_name)


def main() -> None:
    game()
