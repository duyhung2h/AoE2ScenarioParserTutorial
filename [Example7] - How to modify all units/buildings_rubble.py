from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase


class BuildingRubbleInfo(InfoDatasetBase):
    """
    **Description**

    This is an enum class which provides information about most of the building rubbles in the game. Information about the
    following properties of a building is found in this class:
     - Unit ID
     - Icon ID
     - Dead Unit ID
     - HotKey ID
     - If the building is a gaia only unit (eg. ruins)

    **Inherited Methods from class InfoDatasetBase**

    >>> InfoDatasetBase.from_id()
    >>> InfoDatasetBase.from_dead_id()
    >>> InfoDatasetBase.from_icon_id()
    >>> InfoDatasetBase.from_hotkey_id()
    >>> InfoDatasetBase.gaia_only()
    >>> InfoDatasetBase.non_gaia()

    **Examples**

    >>> BuildingRubbleInfo.FENCE_RUBBLE.ID
    >>> 1065

    >>> BuildingRubbleInfo.FENCE_RUBBLE.ICON_ID
    >>> -1

    >>> BuildingRubbleInfo.FENCE_RUBBLE.DEAD_ID
    >>> -1

    >>> BuildingRubbleInfo.FENCE_RUBBLE.HOTKEY_ID
    >>> 16001

    >>> BuildingRubbleInfo.16001.IS_GAIA_ONLY
    >>> False
    """
    FENCE_RUBBLE = 1065, -1, -1, 16001, False
    BARRACKS_DARK_RUBBLE = 1402, -1, -1, 16003, False
    HOUSE_DARK_RUBBLE = 1403, -1, -1, 16003, False
    MILL_DARK_RUBBLE = 1404, -1, -1, 16003, False
    OUTPOST_DARK_RUBBLE = 1405, -1, -1, 16003, False
    GATE_FOUNDATION_RUBBLE = 1406, -1, -1, 16003, False
    PALISADE_WALL_DARK_RUBBLE = 1407, -1, -1, 16003, False
    TOWN_CENTER_DARK_RUBBLE = 1408, -1, -1, 16003, False
    LUMBER_CAMP_RUBBLE = 1409, -1, -1, 16003, False
    MINING_CAMP_RUBBLE = 1410, -1, -1, 16003, False
    MILL_AGE2_RUBBLE = 1411, -1, -1, 16003, False
    MILL_AGE3_RUBBLE = 1412, -1, -1, 16003, False
    BARRACKS_AGE2_RUBBLE = 1413, -1, -1, 16003, False
    BARRACKS_AGE3_RUBBLE = 1414, -1, -1, 16003, False
    ARCHERY_RANGE_AGE2_RUBBLE = 1415, -1, -1, 16003, False
    ARCHERY_RANGE_AGE3_RUBBLE = 1416, -1, -1, 16003, False
    STABLE_AGE2_RUBBLE = 1417, -1, -1, 16003, False
    STABLE_AGE3_RUBBLE = 1418, -1, -1, 16003, False
    BLACKSMITH_AGE2_RUBBLE = 1419, -1, -1, 16003, False
    BLACKSMITH_AGE3_RUBBLE = 1420, -1, -1, 16003, False
    MONASTERY_AGE3_RUBBLE = 1421, -1, -1, 16003, False
    MARKET_AGE2_RUBBLE = 1422, -1, -1, 16003, False
    MARKET_AGE3_RUBBLE = 1423, -1, -1, 16003, False
    MARKET_AGE4_RUBBLE = 1424, -1, -1, 16003, False
    SIEGE_WORKSHOP_AGE2_RUBBLE = 1425, -1, -1, 16003, False
    SIEGE_WORKSHOP_AGE3_RUBBLE = 1426, -1, -1, 16003, False
    UNIVERSITY_AGE3_RUBBLE = 1427, -1, -1, 16003, False
    UNIVERSITY_AGE4_RUBBLE = 1428, -1, -1, 16003, False
    TRADE_WORKSHOP_AGE3_RUBBLE = 1429, -1, -1, 16003, False
    CASTLE_AGE3_RUBBLE = 1430, -1, -1, 16003, False
    TOWN_CENTER_AGE2_RUBBLE = 1431, -1, -1, 16003, False
    TOWN_CENTER_AGE3_RUBBLE = 1432, -1, -1, 16003, False
    TOWN_CENTER_AGE4_RUBBLE = 1433, -1, -1, 16003, False
    HOUSE_AGE2_RUBBLE = 1434, -1, -1, 16003, False
    HOUSE_AGE3_RUBBLE = 1435, -1, -1, 16003, False
    TOWER_AGE2_RUBBLE = 1436, -1, -1, 16003, False
    TOWER_AGE3_RUBBLE = 1437, -1, -1, 16003, False
    TOWER_AGE4_RUBBLE = 1438, -1, -1, 16003, False
    TOWER_BOMBARD_RUBBLE = 1439, -1, -1, 16003, False
    PALISADE_GATE_DARK_NE_RUBBLE = 1440, -1, -1, 16003, False
    PALISADE_GATE_DARK_SE_RUBBLE = 1441, -1, -1, 16003, False
    PALISADE_GATE_DARK_E_RUBBLE = 1442, -1, -1, 16003, False
    PALISADE_GATE_DARK_N_RUBBLE = 1443, -1, -1, 16003, False
    FORTIFIED_TOWER_RUBBLE = 1444, -1, -1, 16003, False
    WONDER_RUBBLE = 1445, -1, -1, 16003, False
    FEITORIA_RUBBLE = 1446, -1, -1, 16003, False
    YURT_A_RUBBLE = 1447, -1, -1, 16003, False
    YURT_B_RUBBLE = 1448, -1, -1, 16003, False
    YURT_C_RUBBLE = 1449, -1, -1, 16003, False
    YURT_D_RUBBLE = 1450, -1, -1, 16003, False
    YURT_E_RUBBLE = 1451, -1, -1, 16003, False
    YURT_F_RUBBLE = 1452, -1, -1, 16003, False
    YURT_G_RUBBLE = 1453, -1, -1, 16003, False
    YURT_H_RUBBLE = 1454, -1, -1, 16003, False
    HUT_A_RUBBLE = 1455, -1, -1, 16003, False
    HUT_B_RUBBLE = 1456, -1, -1, 16003, False
    HUT_C_RUBBLE = 1457, -1, -1, 16003, False
    HUT_D_RUBBLE = 1458, -1, -1, 16003, False
    HUT_E_RUBBLE = 1459, -1, -1, 16003, False
    HUT_F_RUBBLE = 1460, -1, -1, 16003, False
    HUT_G_RUBBLE = 1461, -1, -1, 16003, False
    TENT_A_RUBBLE = 1462, -1, -1, 16003, False
    TENT_B_RUBBLE = 1463, -1, -1, 16003, False
    TENT_C_RUBBLE = 1464, -1, -1, 16003, False
    TENT_D_RUBBLE = 1465, -1, -1, 16003, False
    TENT_E_RUBBLE = 1466, -1, -1, 16003, False
    ARMY_TENT_A_RUBBLE = 1467, -1, -1, 16003, False
    ARMY_TENT_B_RUBBLE = 1468, -1, -1, 16003, False
    ARMY_TENT_C_RUBBLE = 1469, -1, -1, 16003, False
    ARMY_TENT_D_RUBBLE = 1470, -1, -1, 16003, False
    ARMY_TENT_E_RUBBLE = 1471, -1, -1, 16003, False
    BARRICADE_A_RUBBLE = 1472, -1, -1, 16003, False
    BARRICADE_B_RUBBLE = 1473, -1, -1, 16003, False
    BARRICADE_C_RUBBLE = 1474, -1, -1, 16003, False
    BARRICADE_D_RUBBLE = 1475, -1, -1, 16003, False
    PAVILION_A_RUBBLE = 1476, -1, -1, 16003, False
    PAVILION_B_RUBBLE = 1477, -1, -1, 16003, False
    PAVILION_C_RUBBLE = 1478, -1, -1, 16003, False
    KREPOST_RUBBLE = 1479, -1, -1, 16003, False
    CATHEDRAL_RUBBLE = 1480, -1, -1, 16006, False
    TEMPLE_OF_HEAVEN_RUBBLE = 1481, -1, -1, 16006, False
    DOME_OF_ROCK_RUBBLE = 1482, -1, -1, 16006, False
    SHRINE_RUBBLE = 1483, -1, -1, 16003, False
    STORAGE_RUBBLE = 1484, -1, -1, 16003, False
    ARCH_OF_CONSTANTINE_RUBBLE = 1485, -1, -1, 16006, False
    FORTRESS_RUBBLE = 1486, -1, -1, 16003, False
    GOL_GUMBAZ_RUBBLE = 1487, -1, -1, 16006, False
    POENARI_CASTLE_RUBBLE = 1488, -1, -1, 16003, False
    QUIMPER_CATHEDRAL_RUBBLE = 1489, -1, -1, 16006, False
    SANCHI_STUPA_RUBBLE = 1490, -1, -1, 16006, False
    SANKORE_MADRASAH_RUBBLE = 1491, -1, -1, 16006, False
    TOWER_OF_LONDON_RUBBLE = 1492, -1, -1, 16006, False
    DORMITION_CATHEDRAL_RUBBLE = 1493, -1, -1, 16006, False
    THE_ACCURSED_TOWER_RUBBLE = 1494, -1, -1, 16003, False
    THE_TOWER_OF_FLIES_RUBBLE = 1495, -1, -1, 16003, False
    MOSQUE_RUBBLE = 1496, -1, -1, 16006, False
    GRANARY_RUBBLE = 1499, -1, -1, 16003, False
    STONE_GATE_NE_RUBBLE = 1500, -1, -1, 16003, False
    STONE_GATE_SE_RUBBLE = 1501, -1, -1, 16003, False
    STONE_GATE_E_RUBBLE = 1502, -1, -1, 16003, False
    STONE_GATE_N_RUBBLE = 1503, -1, -1, 16003, False
    FORTIFIED_GATE_NE_RUBBLE = 1504, -1, -1, 16003, False
    FORTIFIED_GATE_SE_RUBBLE = 1505, -1, -1, 16003, False
    FORTIFIED_GATE_E_RUBBLE = 1506, -1, -1, 16003, False
    FORTIFIED_GATE_N_RUBBLE = 1507, -1, -1, 16003, False
    STONE_WALL_RUBBLE = 1508, -1, -1, 16003, False
    FORTIFIED_WALL_RUBBLE = 1509, -1, -1, 16003, False
    CITY_GATE_NE_RUBBLE = 1510, -1, -1, 16003, False
    CITY_GATE_SE_RUBBLE = 1511, -1, -1, 16003, False
    CITY_GATE_E_RUBBLE = 1512, -1, -1, 16003, False
    CITY_GATE_N_RUBBLE = 1513, -1, -1, 16003, False
    AMPHITHEATRE_RUBBLE = 1514, -1, -1, 16006, False
    PYRAMID_RUBBLE = 1515, -1, -1, 16006, False
    GREAT_PYRAMID_RUBBLE = 1516, -1, -1, 16006, False
    AACHEN_CATHEDRAL_RUBBLE = 1517, -1, -1, 16006, False
    STONE_GATE_CORNER_RUBBLE = 1518, -1, -1, 16003, False
    FORTIFIED_GATE_CORNER_RUBBLE = 1519, -1, -1, 16003, False
    COLOSSEUM_RUBBLE = 1520, -1, -1, 16006, False
    PALISADE_GATE_CORNER_RUBBLE = 1521, -1, -1, 16003, False
    AQUEDUCT_RUBBLE = 1522, -1, -1, 16003, False
    CITY_GATE_CORNER_RUBBLE = 1523, -1, -1, 16003, False
    DONJON_AGE2_RUBBLE = 1524, -1, -1, 16003, False
    FOLWARK_AGE2_RUBBLE = 1525, -1, -1, 16003, False
    PAGAN_SHRINE_RUBBLE = 1526, -1, -1, 16003, False
    FOLWARK_AGE3_RUBBLE = 1527, -1, -1, 16003, False
    FOLWARK_AGE1_RUBBLE = 1528, -1, -1, 16003, False
    CARAVANSERAI_RUBBLE = 1529, -1, -1, 16003, False
    MINARET_OF_JAM_RUBBLE = 1530, -1, -1, 16006, False
