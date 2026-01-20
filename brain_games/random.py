import random

"""
Модуль инкапсулирует в себе все применения псевдорандома в проекте
Псевдорандом не используется в криптографических целях,
Только в геймплее игр
"""


def randint(begin: int, end: int) -> int:
    return random.randint(begin, end)  # NOSONAR


def sample(population: list, k: int) -> list:
    return random.sample(population, k)  # NOSONAR
