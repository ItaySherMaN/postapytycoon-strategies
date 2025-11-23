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


class ComparisonData:
    def __init__(
        self, strategy_1: NamedStrategy, strategy_2: NamedStrategy, property_id=-1
    ):
        s1_n = normalize(strategy_1.strategy, property_id)
        s2_n = normalize(strategy_2.strategy, property_id)
        diff = s2_n - s1_n  # diff[property_id] == 0
        gold = diff[GOLD_ID]
        pollution = diff[POLLUTION_ID]
        if gold < 0:
            self.from_name = strategy_2.name
            self.to_name = strategy_1.name
            gold = -gold
            pollution = -pollution
        else:
            self.from_name = strategy_1.name
            self.to_name = strategy_2.name
        ratio = (
            (float("inf" if gold >= 0 else "-inf"))
            if pollution == 0
            else gold / pollution
        )
        self.gold = gold
        self.pollution = pollution
        self.ratio = ratio

    def print(self):
        gold_str = ("+" if self.gold >= 0 else "") + to_str(self.gold)
        pollution_str = ("+" if self.pollution >= 0 else "") + to_str(self.pollution)
        ratio_str = to_str(self.ratio)
        print(f"{self.from_name} -> {self.to_name}:")
        print(f"{gold_str} g\t{pollution_str} p\t{ratio_str} g/p")

    def __iter__(self):
        yield self.from_name
        yield self.to_name
        yield self.gold
        yield self.pollution
        yield self.ratio


def calc_comparison_data(s1, s2, property_id=-1):
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
    gold = diff[GOLD_ID]
    pollution = diff[POLLUTION_ID]
    ratio = (
        (float("inf" if gold >= 0 else "-inf")) if pollution == 0 else gold / pollution
    )
    return gold, pollution, ratio


def print_move_data(
    strategy_1: NamedStrategy, strategy_2: NamedStrategy, property_id=-1
):
    ComparisonData(strategy_1, strategy_2, property_id).print()


def print_strategies_absolute_move_data(strategies, property_id=-1):
    for strategy in strategies:
        print_move_data(CURRENT, strategy, property_id)
    print()


def print_strategies_relative_move_data(
    strategies_list, compare_first_to_current=False, property_id=-1
):
    if compare_first_to_current:
        print_move_data(CURRENT, strategies_list[0], property_id)
    for i in range(len(strategies_list) - 1):
        print_move_data(strategies_list[i], strategies_list[i + 1], property_id)
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
    print_strategies_absolute_move_data(PURE_STRATEGIES)


if __name__ == "__main__":
    main()
