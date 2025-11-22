from strategies import *
from normalize import normalize


def print_strategy(s, name):
    """
    Prints the non-zero elements of the strategy with their labels.
    """
    print(f"Strategy: {name}")
    for i in range(len(s)):
        if s[i] != 0:
            print(f"{LABELS[i]}: {to_str(s[i])}")
    print()


def calc_move_data(s1, s2, property_id=-1):
    """
    Computes the gold and pollution we get by moving from strategy `s1` to `s2`,
    where by moving we preseve the property at `property_id`.
    The scale of gold/pollution is per unit of `s1`, replaced by the properly
    scaled `s2`.

    Also returns the move ratio (gold/pollution).
    """
    s1_n = normalize(s1)
    s2_n = normalize(s2)
    v1 = 1 if property_id == -1 else s1[property_id]
    v2 = 1 if property_id == -1 else s2[property_id]
    alpha = 1 if property_id == -1 else v1 / v2
    diff = s2_n * alpha - s1_n  # diff[property_id] == 0
    # diff = normalize(s2, property_id) - normalize(s1, property_id)
    gold = diff[GOLD_ID] / v1  # temp /v1 TODO(sherman): fix
    pollution = diff[POLLUTION_ID] / v1  # temp /v1 TODO(sherman): fix
    ratio = float("inf") if pollution == 0 else gold / pollution
    return gold, pollution, ratio


def print_move_data(s1, s2, name1, name2, property_id=-1):
    gold, pollution, ratio = calc_move_data(s1, s2, property_id)
    gold_str = ("+" if gold >= 0 else "") + to_str(gold)
    pollution_str = ("+" if pollution >= 0 else "") + to_str(pollution)
    print(f"{name1} -> {name2}:")
    print(f"{gold_str} g\t{pollution_str} p\t{to_str(ratio)} g/p")


def print_strategies_absolute_move_data(strategies, property_id=-1):
    for name, strategy in strategies:
        print_move_data(CURRENT.strategy, strategy, CURRENT.name, name, property_id)
    print()


def print_strategies_relative_move_data(
    strategies_list, compare_first_to_current=False, property_id=-1
):
    if compare_first_to_current:
        first_name, first_strategy = strategies_list[0]
        print_move_data(
            CURRENT.strategy, first_strategy, CURRENT.name, first_name, property_id
        )
    for i in range(len(strategies_list) - 1):
        curr_name, corr_strategy = strategies_list[i]
        next_name, next_strategy = strategies_list[i + 1]
        print_move_data(corr_strategy, next_strategy, curr_name, next_name, property_id)
    print()


def main():
    print_strategies_relative_move_data(GOLD_MINE_STRATEGIES)
    print_strategies_relative_move_data(SETTLEMENTS_STRATEGIES)
    print_strategies_relative_move_data(MEGA_CITY_STRATEGIES)
    print_strategies_relative_move_data(ROADS_STRATEGIES)
    print_strategies_relative_move_data(STONE_GAIN_STRATEGIES, property_id=STONE_ID)
    print_strategies_relative_move_data(IRON_GAIN_STRATEGIES, property_id=IRON_ID)
    print_strategies_relative_move_data(WOOD_GAIN_STRATEGIES, property_id=WOOD_ID)
    print_strategies_relative_move_data(CHIPS_GAIN_STRATEGIES, property_id=CHIPS_ID)
    print_strategies_relative_move_data(OIL_GAIN_STRATEGIES, property_id=OIL_ID)
    print_strategies_relative_move_data(
        OIL_STORAGE_STRATEGIES, property_id=OIL_STORAGE_ID
    )
    print_strategies_relative_move_data(
        SHIPYARD_STRATEGIES, compare_first_to_current=True
    )
    print_strategies_relative_move_data(FOOD_STRATEGIES, property_id=FOOD_ID)

    print_strategies_absolute_move_data(PURE_STRATEGIES)


if __name__ == "__main__":
    main()
