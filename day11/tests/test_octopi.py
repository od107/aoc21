from day11.octopi import *


def test_part1():
    assert calc_flashes("day11/data/larger_cave")[0] == 1656
    assert calc_flashes("day11/data/real_data")[0] == 1667


def test_part2():
    assert calc_flashes("day11/data/larger_cave")[1] == 195
    assert calc_flashes("day11/data/real_data")[1] == 488
