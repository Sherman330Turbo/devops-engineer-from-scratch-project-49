import prompt

from brain_games.cli import ask_name, congrats_user, welcome_user

ROUNDS = 3


def engine(game=None) -> None:
    print("Welcome to the Brain Games!")
    user_name = ask_name()
    welcome_user(user_name)

    if not game:
        return

    print(game.DESCRIPTION)

    correct_answers = 0
    while correct_answers < ROUNDS:
        game_round = game.get_round()
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
            print(f"Let's try again, {user_name}!")
            return

    congrats_user(user_name)
