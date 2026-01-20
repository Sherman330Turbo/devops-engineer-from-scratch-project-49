from collections.abc import Callable

import prompt

from brain_games.types import GetRound

ROUNDS = 3


def engine(cli, game: Callable[[], tuple[str, Callable[[], GetRound]]]) -> None:
    rules, get_round_generator = game()
    get_round = get_round_generator()

    print(rules)
    correct_answers = 0
    while correct_answers < ROUNDS:
        game_round = get_round()
        print(f"Question: {game_round['question']}")
        answer = prompt.string("Your answer: ")

        if answer == game_round["answer"]:
            correct_answers += 1
            print("Correct!")
        else:
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {game_round['answer']}."
            )
            print(f"Let's try again, {cli.user_name}!")
            break

    if correct_answers == ROUNDS:
        cli.congrats()
