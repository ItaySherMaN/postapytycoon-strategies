from strategy import *

# 1 food transform into 1/5 gold, but gold from food doesn't get the 10%
# bonus of regular gold income, and we measure income before the 10% bonus.
GOLD_TO_FOOD_RATIO = (1 / 5) / 1.1
AVG_FISHING_SHIP_FOOD = 34
AVG_FISHING_SHIP_GOLD = AVG_FISHING_SHIP_FOOD * GOLD_TO_FOOD_RATIO
AVG_LARGE_FISHING_SHIP_FOOD = 130
AVG_LARGE_FISHING_SHIP_GOLD = AVG_LARGE_FISHING_SHIP_FOOD * GOLD_TO_FOOD_RATIO
FARM_FIELD_FOOD = 26
FARM_FIELD_GOLD = FARM_FIELD_FOOD * GOLD_TO_FOOD_RATIO
AVG_N_FIELDS_IN_FARM = 48
BIG_FARM_FIELD_FOOD = 34
BIG_FARM_FIELD_GOLD = BIG_FARM_FIELD_FOOD * GOLD_TO_FOOD_RATIO
AVG_N_FIELDS_IN_BIG_FARM = 110
MAX_N_FIELDS_IN_BIG_FARM = 120
AVG_N_FIELDS_IN_PUMPKIN_FARM = 40
CARGO_STATION_BONUS = 2.3


# Used for testing pure strategies (whether to use the strategy or not)
CURRENT = NamedStrategy("current", make_strategy())

# Strategies:
CARGO_STATION = NamedStrategy(
    "cargo_station", make_strategy(pollution=180, energy=-120)
)

GOLD_MINE = NamedStrategy("gold_mine", make_strategy(gold=150))
ADVANCED_GOLD_MINE = NamedStrategy(
    "advanced_gold_mine", make_strategy(pollution=5, energy=-50, gold=375)
)
SPECIAL_GOLD_MINE = NamedStrategy("special_gold_mine", make_strategy(gold=375))
HEAVY_GOLD_MINE = NamedStrategy(
    "heavy_gold_mine", make_strategy(pollution=35, energy=-170, gold=600)
)
PREMIUM_GOLD_MINE = NamedStrategy(
    "premium_gold_mine", make_strategy(pollution=10, energy=-10, gold=600)
)
GOLD_MINE_STRATEGIES = [
    GOLD_MINE,
    ADVANCED_GOLD_MINE,
    SPECIAL_GOLD_MINE,
    HEAVY_GOLD_MINE,
    PREMIUM_GOLD_MINE,
]

LEVEL_20 = NamedStrategy("level_20", make_strategy(gold=527))
LEVEL_30 = NamedStrategy(
    "level_30", make_strategy(pollution=117, energy=-267, gold=761)
)
LEVEL_40 = NamedStrategy(
    "level_40", make_strategy(pollution=207, energy=-510, gold=956)
)
LEVEL_50 = NamedStrategy(
    "level_50", make_strategy(pollution=297, energy=-753, gold=1164)
)
LEVEL_55 = NamedStrategy(
    "level_55", make_strategy(pollution=342, energy=-875, gold=1229)
)
LEVEL_66 = NamedStrategy(
    "level_66", make_strategy(pollution=441, energy=-1142, gold=1463)
)
SETTLEMENTS_STRATEGIES = [LEVEL_20, LEVEL_30, LEVEL_40, LEVEL_50, LEVEL_55, LEVEL_66]

MEGA_CITY_33 = NamedStrategy(
    "mega_city_33", make_strategy(pollution=216, energy=-510, gold=3998)
)
MEGA_CITY_60 = NamedStrategy(
    "mega_city_60", make_strategy(pollution=581, energy=-1494, gold=6923)
)
MEGA_CITY_STRATEGIES = [MEGA_CITY_33, MEGA_CITY_60]

DIRT_ROAD = NamedStrategy("dirt_road", make_strategy(land=-1))
PAVED_ROAD = NamedStrategy("paved_road", make_strategy(land=-1, gold=1))
BASIC_ROAD = NamedStrategy("basic_road", make_strategy(pollution=1, land=-1, gold=2))
STREET_ROAD = NamedStrategy("street_road", make_strategy(pollution=2, land=-1, gold=3))
FAST_ROAD = NamedStrategy("fast_road", make_strategy(pollution=5, land=-1, gold=5))

ROADS_STRATEGIES = [
    DIRT_ROAD,
    PAVED_ROAD,
    BASIC_ROAD,
    STREET_ROAD,
    FAST_ROAD,
]

HEAVY_CHIP_FACTORY = NamedStrategy(
    "heavy_chip_factory",
    make_strategy(pollution=400, energy=-700, chips=1200, chips_storage=150000),
)
CARGO_STATION_4_HEAVY_CHIP_FACTORIES = NamedStrategy(
    "cargo_station_4_heavy_chip_factories",
    CARGO_STATION + 4 * with_cargo_station_bonus(HEAVY_CHIP_FACTORY),
)
CHIP_FACTORY = NamedStrategy(
    "chip_factory",
    make_strategy(pollution=75, energy=-200, chips=480, chips_storage=15000),
)
CARGO_STATION_4_CHIP_FACTORIES = NamedStrategy(
    "cargo_station_4_chip_factories",
    CARGO_STATION + 4 * with_cargo_station_bonus(CHIP_FACTORY),
)
SPACE_AGE_FACTORY = NamedStrategy(
    "space_age_factory",
    make_strategy(pollution=100, energy=-200, gold=300, chips=540, chips_storage=50000),
)
CHIPS_GAIN_STRATEGIES = [HEAVY_CHIP_FACTORY, CHIP_FACTORY, SPACE_AGE_FACTORY]

STONE_MINE = NamedStrategy(
    "stone_mine", make_strategy(pollution=2, land=-1, stone=15, stone_storage=4000)
)
MK2_STONE_MINE = NamedStrategy(
    "mk2_stone_mine",
    make_strategy(pollution=5, energy=-20, land=-1, stone=30, stone_storage=16000),
)
STONE_GAIN_STRATEGIES = [STONE_MINE, MK2_STONE_MINE]

FOUNDARY = NamedStrategy(
    "foundary", make_strategy(pollution=65, energy=-25, land=-1, iron_storage=10000)
)
FOUNDARY_IRON_MINE = NamedStrategy(
    "foundary_iron_mine",
    make_strategy(pollution=5, energy=-3, land=-1, iron=10),
)
FOUNDARY_20_MINES = NamedStrategy(
    "foundary_20_mines",
    FOUNDARY + 20 * FOUNDARY_IRON_MINE,
)
HEAVY_FOUNDARY = NamedStrategy(
    "heavy_foundary",
    make_strategy(pollution=300, energy=-250, land=-1, iron_storage=80000),
)
HEAVY_FOUNDARY_IRON_MINE = NamedStrategy(
    "heavy_foundary_iron_mine",
    make_strategy(pollution=5, energy=-3, land=-1, iron=30),
)
HEAVY_FOUNDARY_10_MINES = NamedStrategy(
    "heavy_foundary_10_mines",
    HEAVY_FOUNDARY + 10 * HEAVY_FOUNDARY_IRON_MINE,
)
HEAVY_FOUNDARY_20_MINES = NamedStrategy(
    "heavy_foundary_20_mines",
    HEAVY_FOUNDARY + 20 * HEAVY_FOUNDARY_IRON_MINE,
)
HEAVY_FOUNDARY_30_MINES = NamedStrategy(
    "heavy_foundary_30_mines",
    HEAVY_FOUNDARY + 30 * HEAVY_FOUNDARY_IRON_MINE,
)
HEAVY_FOUNDARY_35_MINES = NamedStrategy(
    "heavy_foundary_35_mines",
    HEAVY_FOUNDARY + 35 * HEAVY_FOUNDARY_IRON_MINE,
)
HEAVY_FOUNDARY_45_MINES = NamedStrategy(
    "heavy_foundary_45_mines",
    HEAVY_FOUNDARY + 45 * HEAVY_FOUNDARY_IRON_MINE,
)
IRON_GAIN_STRATEGIES = [
    FOUNDARY_20_MINES,
    HEAVY_FOUNDARY_10_MINES,
    HEAVY_FOUNDARY_20_MINES,
    HEAVY_FOUNDARY_30_MINES,
    HEAVY_FOUNDARY_35_MINES,
    HEAVY_FOUNDARY_45_MINES,
]

LUMBER_MILL = NamedStrategy(
    "lumber_mill", make_strategy(land=-1, lumber=2 * 24, lumber_storage=500)
)
INDUSTRIAL_MILL = NamedStrategy(
    "industrial_mill",
    make_strategy(
        pollution=15, energy=-20, land=-1, lumber=4 * 80, lumber_storage=1500
    ),
)
PREMIUM_LUMBER_MILL = NamedStrategy(
    "premium_lumber_mill", make_strategy(land=-1, lumber=14 * 80, lumber_storage=25000)
)
LUMBER_GAIN_STRATEGIES = [LUMBER_MILL, INDUSTRIAL_MILL, PREMIUM_LUMBER_MILL]

OIL_STORAGE = NamedStrategy("oil_storage", make_strategy(land=-1, oil_storage=7500))
OIL_TANKER = NamedStrategy(
    "oil_tanker", make_strategy(pollution=5, sea=-1, oil_storage=4000)
)
OIL_STORAGE_STRATEGIES = [OIL_STORAGE, OIL_TANKER]

ONSHORE_OIL_RIG = NamedStrategy(
    "onshore_oil_rig",
    make_strategy(pollution=5 + 10, energy=-10, land=-1, oil=10, oil_storage=6800),
)
# offshore_oil_rig scale is 40 ONLY when next to an oil_tanker,
# otherwise it is 20 and I'm not even considering it because it's very bad
OFFSHORE_OIL_RIG = NamedStrategy(
    "offshore_oil_rig",
    make_strategy(pollution=45 + 60, energy=30, sea=-1, oil=40, oil_storage=5000),
)
OFFSHORE_OIL_RIG_WITH_OIL_TANKER = NamedStrategy(
    "offshore_oil_rig_with_oil_tanker",
    OFFSHORE_OIL_RIG + OIL_TANKER,
)
OIL_GAIN_STRATEGIES = [
    ONSHORE_OIL_RIG,
    OFFSHORE_OIL_RIG_WITH_OIL_TANKER,
    OFFSHORE_OIL_RIG,
]

SMALL_SHIPYARD = NamedStrategy(
    "small_shipyard",
    make_strategy(pollution=5, sea=-1, fishing_ship=1, gold=0),
)
HEAVY_SHIPYARD = NamedStrategy(
    "heavy_shipyard",
    make_strategy(
        pollution=75,
        energy=-150,
        sea=-1,
        fishing_ship=4,
        gold=150,
    ),
)
SHIPYARD_STRATEGIES = [SMALL_SHIPYARD, HEAVY_SHIPYARD]


FARM = NamedStrategy(
    "farm",
    make_strategy(land=-1),
)
FARM_FIELD = NamedStrategy(
    "farm_field",
    make_strategy(
        pollution=-3,
        land=-1,
        gold=FARM_FIELD_GOLD,
        food=FARM_FIELD_FOOD,
    ),
)
FARM_WITH_FIELDS = NamedStrategy(
    "farm_with_fields",
    FARM + AVG_N_FIELDS_IN_FARM * FARM_FIELD,
)
BIG_FARM = NamedStrategy("big_farm", make_strategy(energy=-3, land=-1))
BIG_FARM_FIELD = NamedStrategy(
    "big_farm_field",
    make_strategy(
        pollution=-3,
        land=-1,
        gold=BIG_FARM_FIELD_GOLD,
        food=BIG_FARM_FIELD_FOOD,
    ),
)
BIG_FARM_WITH_FIELDS = NamedStrategy(
    "big_farm_with_fields",
    BIG_FARM + AVG_N_FIELDS_IN_BIG_FARM * BIG_FARM_FIELD,
)
BIG_FARM_WITH_MAX_FIELDS = NamedStrategy(
    "big_farm_with_max_fields",
    BIG_FARM + MAX_N_FIELDS_IN_BIG_FARM * BIG_FARM_FIELD,
)
PUMPKIN_FARM = NamedStrategy("pumpkin_farm", make_strategy(land=-1, gold=200))
PUMPKIN_FARM_WITH_FIELDS = NamedStrategy(
    "pumpkin_farm_with_fields",
    PUMPKIN_FARM + AVG_N_FIELDS_IN_PUMPKIN_FARM * BIG_FARM_FIELD,
)
FISHING_SHIP = NamedStrategy(
    "fishing_ship",
    make_strategy(
        sea=-1, fishing_ship=-1, gold=AVG_FISHING_SHIP_GOLD, food=AVG_FISHING_SHIP_FOOD
    ),
)
LARGE_FISHING_SHIP = NamedStrategy(
    "large_fishing_ship",
    make_strategy(
        pollution=10,
        sea=-1,
        gold=AVG_LARGE_FISHING_SHIP_GOLD,
        food=AVG_LARGE_FISHING_SHIP_FOOD,
    ),
)
FOOD_STRATEGIES = [
    FARM_WITH_FIELDS,
    BIG_FARM_WITH_FIELDS,
    BIG_FARM_WITH_MAX_FIELDS,
    PUMPKIN_FARM_WITH_FIELDS,
    FISHING_SHIP,
    LARGE_FISHING_SHIP,
]

# Pure-strategies: They are only used for getting gold, energy, or reducing pollution.
SWEPT_OCEAN = NamedStrategy("swept_ocean", make_strategy(gold=3, sea=-1))
SMALL_FOREST = NamedStrategy(
    "small_forest", make_strategy(pollution=-1, land=-1, gold=1)
)
DENSE_FOREST = NamedStrategy(
    "dense_forest", make_strategy(pollution=-2, land=-1, gold=2)
)
DEEP_FOREST = NamedStrategy("deep_forest", make_strategy(pollution=-3, land=-1, gold=4))
COAL_PLANT = NamedStrategy(
    "coal_plant", make_strategy(pollution=80, energy=210, land=-1)
)
WIND_MILL = NamedStrategy("wind_mill", make_strategy(pollution=1, energy=20, land=-1))
ADVANCED_WIND_MILL = NamedStrategy(
    "advanced_wind_mill", make_strategy(energy=28, land=-1)
)
SOLAR_PANELS = NamedStrategy("solar_panels", make_strategy(energy=15, gold=2, land=-1))
GOLD_PLATED_SOLAR_PANELS = NamedStrategy(
    "gold_plated_solar_panels", make_strategy(energy=500, gold=2000, land=-1)
)
THERMAL_PLANT = NamedStrategy(
    "thermal_plant", make_strategy(pollution=5, energy=450, land=-1)
)
THERMAL_PLANT_WITH_5_FAST_ROADS = NamedStrategy(
    "thermal_plant_with_5_fast_roads",
    THERMAL_PLANT + 5 * FAST_ROAD,
)
THERMAL_PLANT_WITH_9_FAST_ROADS = NamedStrategy(
    "thermal_plant_with_9_fast_roads",
    THERMAL_PLANT + 9 * FAST_ROAD,
)
THERMAL_PLANT_WITH_10_FAST_ROADS = NamedStrategy(
    "thermal_plant_with_10_fast_roads",
    THERMAL_PLANT + 10 * FAST_ROAD,
)
# Used for ignoring the fishing ships
IGNORE_FISHING_SHIP = NamedStrategy(
    "ignore_fishing_ship", make_strategy(fishing_ship=-1)
)
PURE_STRATEGIES = [
    SMALL_FOREST,
    DENSE_FOREST,
    DEEP_FOREST,
    COAL_PLANT,
    WIND_MILL,
    ADVANCED_WIND_MILL,
    SOLAR_PANELS,
    GOLD_PLATED_SOLAR_PANELS,
    THERMAL_PLANT,
    THERMAL_PLANT_WITH_5_FAST_ROADS,
    THERMAL_PLANT_WITH_9_FAST_ROADS,
    THERMAL_PLANT_WITH_10_FAST_ROADS,
    IGNORE_FISHING_SHIP,
] + FOOD_STRATEGIES  # food strategies are also pure strategies

STORAGE_CRANE = NamedStrategy(
    "storage_crane",
    make_strategy(
        pollution=12,
        energy=-12,
        stone_storage=10000,
        lumber_storage=8000,
        iron_storage=7000,
        chips_storage=20000,
    ),
)
URANIUM_REFINERY = NamedStrategy(
    "uranium_refinery",
    make_strategy(pollution=400, energy=-100, ubatteries=3, ubatteries_storage=120),
)


# Choose current best strategies for normalization
CURRENT_ENERGY_STRATEGY = ADVANCED_WIND_MILL
CURRENT_LAND_STRATEGY = BIG_FARM_WITH_FIELDS
CURRENT_SEA_STRATEGY = SWEPT_OCEAN
CURRENT_FISHING_SHIP_STRATEGY = FISHING_SHIP
