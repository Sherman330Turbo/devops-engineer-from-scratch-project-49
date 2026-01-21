import argparse

from brain_games.cli import ask_name, welcome_user
from brain_games.scripts.engine import engine
from brain_games.scripts.games.calc import calc_game
from brain_games.scripts.games.gcd import gcd_game
from brain_games.scripts.games.is_even import is_even_game
from brain_games.scripts.games.is_prime import is_prime_game
from brain_games.scripts.games.progression import progression_game


def run(game) -> None:
    print("Welcome to the Brain Games!")
    user_name = ask_name()
    welcome_user(user_name)

    match game:
        case "even":
            engine(user_name, is_even_game)
        case "calc":
            engine(user_name, calc_game)
        case "gcd":
            engine(user_name, gcd_game)
        case "progression":
            engine(user_name, progression_game)
        case "prime":
            engine(user_name, is_prime_game)


def main() -> None:
    parser = argparse.ArgumentParser(prog="brain-games")
    parser.add_argument(
        "--game",
        choices=("even", "calc"),
        default=None,
    )

    args = parser.parse_args()
    run(args.game)


def run_even_game() -> None:
    run("even")


def run_calc_game() -> None:
    run("calc")


def run_gcd_game() -> None:
    run("gcd")


def run_progression_game() -> None:
    run("progression")


def run_prime_game() -> None:
    run("prime")
