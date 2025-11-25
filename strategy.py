import numpy as np
from utils import to_str

POLLUTION_ID = 0
ENERGY_ID = 1
LAND_ID = 2
SEA_ID = 3
FISHING_SHIP_ID = 4
GOLD_ID = 5
LUMBER_ID = 6
LUMBER_STORAGE_ID = 7
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

STORAGE_IDS = [
    LUMBER_STORAGE_ID,
    STONE_STORAGE_ID,
    IRON_STORAGE_ID,
    CHIPS_STORAGE_ID,
    OIL_STORAGE_ID,
    UBATTERIES_STORAGE_ID,
]
DEFAULT_STORAGE_BONUS = 1.1

LABELS = [
    "POLLUTION_ID",
    "ENERGY_ID",
    "LAND_ID",
    "SEA_ID",
    "FISHING_SHIP_ID",
    "GOLD_ID",
    "LUMBER_ID",
    "LUMBER_STORAGE_ID",
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


def make_strategy(
    pollution=0,
    energy=0,
    land=0,
    sea=0,
    fishing_ship=0,
    gold=0,
    lumber=0,
    lumber_storage=0,
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
    strategy[LUMBER_ID] = lumber
    strategy[LUMBER_STORAGE_ID] = lumber_storage
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
    apply_storage_bonus(strategy, DEFAULT_STORAGE_BONUS)
    return strategy


def apply_storage_bonus(strategy, storage_bonus):
    s = get_strategy(strategy)
    for storage_id in STORAGE_IDS:
        s[storage_id] *= storage_bonus


def with_storage_bonus(strategy, storage_bonus):
    s = np.copy(get_strategy(strategy))
    apply_storage_bonus(s, storage_bonus)
    return s


def print_strategy(strategy):
    """
    Prints the non-zero elements of the strategy with their labels.
    """
    name = strategy.name if isinstance(strategy, NamedStrategy) else ""
    s = get_strategy(strategy)
    print(f"Strategy: {name}")
    for property_id in range(len(s)):
        if s[property_id] != 0:
            print(f"{LABELS[property_id]}: {to_str(s[property_id])}")
    print()


class NamedStrategy:
    def __init__(self, name: str, strategy: np.ndarray):
        self.name = name
        self.strategy = np.asarray(strategy)

    def __array__(self, dtype=None):
        return np.asarray(self.strategy, dtype=dtype)

    def __add__(self, other):
        return np.add(self.strategy, other)

    def __mul__(self, other):
        return np.multiply(self.strategy, other)

    def __rmul__(self, other):
        return np.multiply(other, self.strategy)

    @property
    def shape(self):
        return self.strategy.shape

    @property
    def dtype(self):
        return self.strategy.dtype

    def __getitem__(self, item):
        """Indexing returns the underlying ndarray directly."""
        return self.strategy[item]

    def __repr__(self):
        return f"NamedStrategy(name={self.name!r}, strategy={self.strategy!r})"

    def __iter__(self):
        yield self.name
        yield self.strategy


def get_strategy(strategy: NamedStrategy | np.ndarray):
    return strategy.strategy if isinstance(strategy, NamedStrategy) else strategy


def remove_property_with(strategy, property_id, normalizer):
    """
    Returns a copy of the strategy without the specified property component.
    """
    s = get_strategy(strategy)
    n = get_strategy(normalizer)
    return s - n * (s[property_id] / n[property_id])


def with_cargo_station_bonus(strategy):
    CARGO_STATION_BONUS = 2.3
    s = np.copy(get_strategy(strategy))
    s[LUMBER_ID] *= CARGO_STATION_BONUS
    s[STONE_ID] *= CARGO_STATION_BONUS
    s[IRON_ID] *= CARGO_STATION_BONUS
    s[CHIPS_ID] *= CARGO_STATION_BONUS
    s[OIL_ID] *= CARGO_STATION_BONUS
    s[UBATTERIES_ID] *= CARGO_STATION_BONUS
    return s


def scale_to(strategy, property_id, new_scale):
    """
    Returns a copy of the strategy scaled to new_scale.
    """
    s = get_strategy(strategy)
    old_scale = s[property_id]
    assert old_scale != 0, "Cannot scale strategy with zero property value."
    return s * (new_scale / old_scale)
