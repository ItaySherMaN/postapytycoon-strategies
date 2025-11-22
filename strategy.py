from utils import to_str
import numpy as np

POLLUTION_ID = 0
ENERGY_ID = 1
LAND_ID = 2
SEA_ID = 3
FISHING_SHIP_ID = 4
GOLD_ID = 5
WOOD_ID = 6
WOOD_STORAGE_ID = 7
STONE_ID = 8
STONE_STORAGE_ID = 9
IRON_ID = 10
IRON_STORAGE_ID = 11
CHIPS_ID = 12
CHIPS_STORAGE_ID = 13
OIL_ID = 14
OIL_STORAGE_ID = 15
UBATTERIES_ID = 16
UBATTERIES_STORAGE_ID = 17
FOOD_ID = 18

LABELS = [
    "POLLUTION_ID",
    "ENERGY_ID",
    "LAND_ID",
    "SEA_ID",
    "FISHING_SHIP_ID",
    "GOLD_ID",
    "WOOD_ID",
    "WOOD_STORAGE_ID",
    "STONE_ID",
    "STONE_STORAGE_ID",
    "IRON_ID",
    "IRON_STORAGE_ID",
    "CHIPS_ID",
    "CHIPS_STORAGE_ID",
    "OIL_ID",
    "OIL_STORAGE_ID",
    "UBATTERIES_ID",
    "UBATTERIES_STORAGE_ID ",
    "FOOD_ID",
]


def get_strategy(
    pollution=0,
    energy=0,
    land=0,
    sea=0,
    fishing_ship=0,
    gold=0,
    wood=0,
    wood_storage=0,
    stone=0,
    stone_storage=0,
    iron=0,
    iron_storage=0,
    chips=0,
    chips_storage=0,
    oil=0,
    oil_storage=0,
    ubatteries=0,
    ubatteries_storage=0,
    food=0,
):
    strategy = np.empty(len(LABELS))
    strategy[POLLUTION_ID] = pollution
    strategy[ENERGY_ID] = energy
    strategy[LAND_ID] = land
    strategy[SEA_ID] = sea
    strategy[FISHING_SHIP_ID] = fishing_ship
    strategy[GOLD_ID] = gold
    strategy[WOOD_ID] = wood
    strategy[WOOD_STORAGE_ID] = wood_storage
    strategy[STONE_ID] = stone
    strategy[STONE_STORAGE_ID] = stone_storage
    strategy[IRON_ID] = iron
    strategy[IRON_STORAGE_ID] = iron_storage
    strategy[CHIPS_ID] = chips
    strategy[CHIPS_STORAGE_ID] = chips_storage
    strategy[OIL_ID] = oil
    strategy[OIL_STORAGE_ID] = oil_storage
    strategy[UBATTERIES_ID] = ubatteries
    strategy[UBATTERIES_STORAGE_ID] = ubatteries_storage
    strategy[FOOD_ID] = food
    return strategy


def remove_property_with(strategy, property_id, normalizer):
    """
    Returns a copy of the strategy without the specified property component.
    """
    return strategy - normalizer * (strategy[property_id] / normalizer[property_id])


def scale_to(strategy, property_id, new_scale):
    """
    Returns a copy of the strategy scaled to new_scale.
    """
    old_scale = strategy[property_id]
    return strategy * (new_scale / old_scale)


class NamedStrategy:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def __iter__(self):
        yield self.name
        yield self.strategy
