from day12.caves import *


def test_part1():
    assert calc_paths("day11/data/simple_cave") == 10
    assert calc_paths("day11/data/less_simple_cave") == 19
    assert calc_paths("day11/data/larger_cave") == 226
    # assert calc_paths("day11/data/real_data") == 1667

#
# def test_part2():
#     assert calc_flashes("day11/data/larger_cave")[1] == 195
#     assert calc_flashes("day11/data/real_data")[1] == 488
