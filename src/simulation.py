import random
import uuid
from math import isqrt

from src._collections.chip_collection import ChipCollection
from src.common.config import logger
from src.common.exceptions import NegativeArgumentException
from src.objects.chip import Chip
from src.objects.goose import HonkGoose, Goose, WarGoose
from src.objects.player import Player
from src.objects.casino import Casino

GOOSES_CLASSES = (HonkGoose, WarGoose)


def generate_random_name(length: int) -> str:
    return str(uuid.UUID(int=random.getrandbits(128)))[:length]


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
    if steps < 0:
        raise NegativeArgumentException(run_simulation)
    n = max(2, isqrt(steps))
    casino = Casino()
    for _ in range(n):
        chips = ChipCollection()
        for __ in range(random.randint(1, 10)):
            chips.append(Chip(random.randint(1, 1000)))
        casino.register_player(Player(generate_random_name(6), chips))
        goose_type = random.choice(GOOSES_CLASSES)
        goose = goose_type(name=generate_random_name(6), honk_volume=random.randint(1, 100))
        if isinstance(goose_type, WarGoose):
            goose.damage = random.randint(1, 100)
        casino.register_goose(goose)
    for step in range(steps):
        if len(casino.players) == 0:
            logger.info(f"Гуси победили за {step} шагов! Люди всё проиграли в казино")
            return
        casino.step()
    casino.casino_balances.print_rating()
