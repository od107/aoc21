from day5.vents import *


def test_vents():
    assert vents("day5/data/larger_cave") == 5
    assert vents("day5/data/real_data") == 7438


def test_vent_diag():
    assert vents("day5/data/larger_cave", False) == 12
    assert vents("day5/data/real_data", False) == 21406