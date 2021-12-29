from day13.origami import *


def test_part1():
    assert origami("day12/data/test_data", 1) == 17
    assert origami("day12/data/real_data", 1) == 631
