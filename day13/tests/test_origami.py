from day13.origami import *


def test_part1():
    assert origami("day13/data/test_data", 1) == 17
    assert origami("day13/data/real_data", 1) == 631
