import argparse

from brain_games.cli import Cli
from brain_games.scripts.engine import engine
from brain_games.scripts.games.calc import calc_game
from brain_games.scripts.games.is_even import is_even_game


def run(game) -> None:
    cli = Cli()
    cli.ask_name()
    cli.welcome()

    match game:
        case "even":
            engine(cli, is_even_game)
        case "calc":
            engine(cli, calc_game)


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
