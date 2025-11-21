from strategies import (
    without_scale,
    scale_to,
    CURRENT_ENERGY_STRATEGY,
    CURRENT_LAND_STRATEGY,
    CURRENT_SEA_STRATEGY,
    CURRENT_FISHING_SHIP_STRATEGY,
    ENERGY_ID,
    LAND_ID,
    SEA_ID,
    FISHING_SHIP_ID,
)
import numpy as np


ENERGY_NORMALIZER = without_scale(CURRENT_ENERGY_STRATEGY)


def without_energy(strategy):
    """
    Returns a copy of the strategy without energy component.
    """
    global ENERGY_NORMALIZER
    s = np.copy(strategy)
    s -= ENERGY_NORMALIZER * (s[ENERGY_ID] / ENERGY_NORMALIZER[ENERGY_ID])
    return s


LAND_NORMALIZER = without_energy(without_scale(CURRENT_LAND_STRATEGY))


def without_land(strategy):
    """
    Returns a copy of the strategy without land component.
    """
    global LAND_NORMALIZER
    s = np.copy(strategy)
    s -= LAND_NORMALIZER * (s[LAND_ID] / LAND_NORMALIZER[LAND_ID])
    return s


SEA_NORMALIZER = without_land(without_energy(without_scale(CURRENT_SEA_STRATEGY)))


def without_sea(strategy):
    """
    Returns a copy of the strategy without sea component.
    """
    global SEA_NORMALIZER
    s = np.copy(strategy)
    s -= SEA_NORMALIZER * (s[SEA_ID] / SEA_NORMALIZER[SEA_ID])
    return s


FISHING_SHIP_NORMALIZER = without_sea(
    without_land(without_energy(without_scale(CURRENT_FISHING_SHIP_STRATEGY)))
)


def without_fishing_ship(strategy):
    """
    Returns a copy of the strategy without fishing ship component.
    """
    global FISHING_SHIP_NORMALIZER
    s = np.copy(strategy)
    s -= FISHING_SHIP_NORMALIZER * (
        s[FISHING_SHIP_ID] / FISHING_SHIP_NORMALIZER[FISHING_SHIP_ID]
    )
    return s


def normalize(s):
    # remove energy
    s = without_energy(s)
    # remove land
    s = without_land(s)
    # remove sea
    s = without_sea(s)
    # remove fishing ship
    s = without_fishing_ship(s)
    return scale_to(s, 1.0)
