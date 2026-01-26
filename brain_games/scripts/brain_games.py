from brain_games.cli import ask_name, welcome_user
from brain_games.engine import engine
from brain_games.games import calc, gcd, is_even, is_prime, progression


def run(game=None) -> None:
    print("Welcome to the Brain Games!")
    user_name = ask_name()
    welcome_user(user_name)

    match game:
        case "even":
            engine(user_name, is_even)
        case "calc":
            engine(user_name, calc)
        case "gcd":
            engine(user_name, gcd)
        case "progression":
            engine(user_name, progression)
        case "prime":
            engine(user_name, is_prime)


def main() -> None:
    run()
