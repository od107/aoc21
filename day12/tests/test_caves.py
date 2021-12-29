from day12.caves import *


def test_part1():
    assert calc_paths("day12/data/simple_cave") == 10
    assert calc_paths("day12/data/less_simple_cave") == 19
    assert calc_paths("day12/data/larger_cave") == 226
    assert calc_paths("day12/data/real_data") == 3410


def test_part2():
    assert calc_paths("day12/data/simple_cave", True) == 36
    assert calc_paths("day12/data/less_simple_cave", True) == 103
    assert calc_paths("day12/data/larger_cave", True) == 3509
    assert calc_paths("day12/data/real_data", True) == 98796
