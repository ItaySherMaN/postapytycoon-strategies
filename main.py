from strategies import *
from normalize import normalize
from utils import to_str, safe_divide


class ComparisonData:
    """
    Holds data about moving from one strategy to another.
    Computes the gold and pollution we get by moving from strategy `s1` to `s2`,
    where by moving we preseve the property at `property_id`.

    The scale of gold/pollution is per unit of `property_id`

    If moving from s1 to s2 results in negative gold, the direction is reversed.
    """

    def __init__(
        self, strategy_1: NamedStrategy, strategy_2: NamedStrategy, property_id=-1
    ):
        s1_n = normalize(strategy_1, property_id)
        s2_n = normalize(strategy_2, property_id)
        diff = s2_n - s1_n  # diff[property_id] == 0
        self.from_name = strategy_1.name
        self.to_name = strategy_2.name
        self.gold = diff[GOLD_ID]
        self.pollution = diff[POLLUTION_ID]
        self.ratio = safe_divide(self.pollution, self.gold)
        if self.gold < 0 or (self.gold == 0 and self.pollution > 0):
            # reverse direction to prioritise gold gain and after that pollution decrease
            self.from_name, self.to_name = self.to_name, self.from_name
            self.gold, self.pollution = -self.gold, -self.pollution

    def print(self):
        gold_str = ("+" if self.gold >= 0 else "") + to_str(self.gold)
        pollution_str = ("+" if self.pollution >= 0 else "") + to_str(self.pollution)
        ratio_str = to_str(self.ratio)
        print(f"{self.from_name} -> {self.to_name}:")
        print(f"{gold_str} g\t{pollution_str} p\t{ratio_str} p/g")

    def __iter__(self):
        yield self.from_name
        yield self.to_name
        yield self.gold
        yield self.pollution
        yield self.ratio

    def __eq__(self, other):
        return (
            self.from_name == other.from_name
            and self.to_name == other.to_name
            and self.gold == other.gold
            and self.pollution == other.pollution
            and self.ratio == other.ratio
        )

    def __hash__(self):
        return hash((self.from_name, self.to_name))


def print_comparison_data(
    strategy_1: NamedStrategy, strategy_2: NamedStrategy, property_id=-1
):
    ComparisonData(strategy_1, strategy_2, property_id).print()


def gather_relative_comparison_datas(
    strategies_list, comparisons_set, compare_first_to_current=False, property_id=-1
):
    """
    Gathers comparison data for moving between consecutive strategies in
    strategies_list, and puts the comparison datas in the comparisons_set.
    """
    if compare_first_to_current:
        data = ComparisonData(CURRENT, strategies_list[0], property_id)
        comparisons_set.add(data)
    for i in range(len(strategies_list) - 1):
        data = ComparisonData(strategies_list[i], strategies_list[i + 1], property_id)
        comparisons_set.add(data)


def gather_absolute_comparison_datas(strategies, comparisons_set, property_id=-1):
    """
    Gathers comparison data for moving from CURRENT to each strategy in
    strategies, and puts the comparison datas in the comparisons_set.
    """
    for strategy in strategies:
        data = ComparisonData(CURRENT, strategy, property_id)
        comparisons_set.add(data)


def divide_comparison_datas(comparison_datas):
    """
    Divides the comparison datas into two lists:
    - MUST_BUY: those with negative ratio (i.e., for every gold we get, pollution decreases)
    - TRADE_OFF: those with positive ratio (i.e, the deal is for every gold we get, pollution increases)

    Both lists will be sorted from best to worst ratio (small to large).
    """
    must_buy = []
    trade_off = []
    for data in comparison_datas:
        if data.ratio <= 0:
            must_buy.append(data)
        else:
            trade_off.append(data)
    comparison_func = lambda comparison_data: comparison_data.ratio
    must_buy.sort(key=comparison_func)
    trade_off.sort(key=comparison_func)
    return must_buy, trade_off


def main():
    comparisons_set = set()
    gather_relative_comparison_datas(GOLD_MINE_STRATEGIES, comparisons_set)
    gather_relative_comparison_datas(SETTLEMENTS_STRATEGIES, comparisons_set)
    gather_relative_comparison_datas(MEGA_CITY_STRATEGIES, comparisons_set)
    gather_relative_comparison_datas(ROADS_STRATEGIES, comparisons_set)
    gather_relative_comparison_datas(
        STONE_GAIN_STRATEGIES, comparisons_set, property_id=STONE_ID
    )
    gather_relative_comparison_datas(
        IRON_GAIN_STRATEGIES, comparisons_set, property_id=IRON_ID
    )
    gather_relative_comparison_datas(
        LUMBER_GAIN_STRATEGIES, comparisons_set, property_id=LUMBER_ID
    )
    gather_relative_comparison_datas(
        CHIPS_GAIN_STRATEGIES, comparisons_set, property_id=CHIPS_ID
    )
    gather_relative_comparison_datas(
        OIL_GAIN_STRATEGIES, comparisons_set, property_id=OIL_ID
    )
    gather_relative_comparison_datas(
        OIL_STORAGE_STRATEGIES, comparisons_set, property_id=OIL_STORAGE_ID
    )
    gather_relative_comparison_datas(
        SHIPYARD_STRATEGIES, comparisons_set, compare_first_to_current=True
    )
    gather_absolute_comparison_datas(PURE_STRATEGIES, comparisons_set)

    must_buy, trade_off = divide_comparison_datas(comparisons_set)

    print("Must buy:")
    for comparison_data in must_buy:
        comparison_data.print()
    print()

    print("Trade off:")
    for comparison_data in trade_off:
        comparison_data.print()

    num_complex_gold_mine = 1
    num_super_eco_storage_with_pavement = 1
    num_eco_storage_with_pavement = 9
    num_premium_storage_with_pavement = 9
    num_oil_storage = 2344
    num_storage_container_400 = 4521
    num_steel_storage = 78
    num_heavy_chip_factory = 0
    num_industrial_mill = 31
    num_premium_lumber_mill = 6
    num_uranium_refinery = 3
    num_mk2_stone_mine = 651
    num_heavy_foundary_iron_mine = 760
    num_heavy_foundary_hybrid_mine = 17
    num_shipyard_storage = 118
    num_heavy_foundary = 24
    num_chip_factory = 152
    num_space_age_factory = 11
    num_onshore_oil_rig = 1145
    num_rift_oil_rig = 2
    num_storage_crane = 1353
    total_production = (
        num_complex_gold_mine * COMPLEX_GOLD_MINE
        + num_super_eco_storage_with_pavement * SUPER_ECO_STORAGE_WITH_PAVEMENT
        + num_eco_storage_with_pavement * ECO_STORAGE_WITH_PAVEMENT
        + num_premium_storage_with_pavement * PREMIUM_STORAGE_WITH_PAVEMENT
        + num_oil_storage * OIL_STORAGE
        + num_storage_container_400 * STORAGE_CONTAINER_400
        + num_steel_storage * STEEL_STORAGE
        + num_heavy_chip_factory * HEAVY_CHIP_FACTORY
        + num_industrial_mill * INDUSTRIAL_MILL
        + num_premium_lumber_mill * PREMIUM_LUMBER_MILL
        + num_uranium_refinery * URANIUM_REFINERY
        + num_mk2_stone_mine * MK2_STONE_MINE
        + num_heavy_foundary_iron_mine * HEAVY_FOUNDARY_IRON_MINE
        + num_heavy_foundary_hybrid_mine * HEAVY_FOUNDARY_HYBRID_MINE
        + num_shipyard_storage * SHIPYARD_STORAGE
        + num_heavy_foundary * HEAVY_FOUNDARY
        + num_chip_factory * CHIP_FACTORY
        + num_space_age_factory * SPACE_AGE_FACTORY
        + num_onshore_oil_rig * ONSHORE_OIL_RIG
        + num_rift_oil_rig * RIFT_OIL_RIG
        + num_storage_crane * STORAGE_CRANE
    )
    print_strategy(total_production)
    print_strategy(normalize(total_production))
    # print_strategy(STORAGE_CONTAINER_400)
    # print_strategy(STORAGE_CRANE)
    # print_strategy(SHIPYARD_STORAGE)
    # print_strategy(MK2_STONE_MINE)
    # print_strategy(COMPLEX_GOLD_MINE)


if __name__ == "__main__":
    main()
