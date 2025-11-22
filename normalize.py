from strategy import (
    remove_property_with,
    scale_to,
    ENERGY_ID,
    LAND_ID,
    SEA_ID,
    FISHING_SHIP_ID,
)
from strategies import (
    CURRENT_ENERGY_STRATEGY,
    CURRENT_LAND_STRATEGY,
    CURRENT_SEA_STRATEGY,
    CURRENT_FISHING_SHIP_STRATEGY,
)
import numpy as np


ENERGY_NORMALIZER = CURRENT_ENERGY_STRATEGY


def remove_energy(strategy):
    """
    Returns a copy of the strategy without energy component.
    """
    return remove_property_with(strategy, ENERGY_ID, ENERGY_NORMALIZER)


LAND_NORMALIZER = remove_energy(CURRENT_LAND_STRATEGY)


def remove_land(strategy):
    """
    Returns a copy of the strategy without land component.
    """
    return remove_property_with(strategy, LAND_ID, LAND_NORMALIZER)


SEA_NORMALIZER = remove_land(remove_energy(CURRENT_SEA_STRATEGY))


def remove_sea(strategy):
    """
    Returns a copy of the strategy without sea component.
    """
    return remove_property_with(strategy, SEA_ID, SEA_NORMALIZER)


FISHING_SHIP_NORMALIZER = remove_sea(
    remove_land(remove_energy(CURRENT_FISHING_SHIP_STRATEGY))
)


def remove_fishing_ship(strategy):
    """
    Returns a copy of the strategy without fishing ship component.
    """
    return remove_property_with(strategy, FISHING_SHIP_ID, FISHING_SHIP_NORMALIZER)


def normalize(s, property_id=-1):
    # remove energy
    s = remove_energy(s)
    # remove land
    s = remove_land(s)
    # remove sea
    s = remove_sea(s)
    # remove fishing ship
    s = remove_fishing_ship(s)
    return s if property_id == -1 else scale_to(s, property_id, 1.0)
