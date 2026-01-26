import random
from typing import TypeVar

"""
Модуль инкапсулирует в себе все применения псевдорандома в проекте
Псевдорандом не используется в криптографических целях,
Только в геймплее игр
"""

T = TypeVar("T")


def randint(begin: int, end: int) -> int:
    return random.randint(begin, end)  # NOSONAR


def choice(population: list[T]) -> T:
    return random.choice(population)  # NOSONAR
