from day6.fish import *


def test_fish():
    assert fish("day6/data/larger_cave", 18) == 26
    assert fish("day6/data/larger_cave", 80) == 5934
    assert fish("day6/data/real_data", 80) == 352151


def test_fish_fast():
    assert fish_fast("day6/data/larger_cave", 18) == 26
    assert fish_fast("day6/data/larger_cave", 80) == 5934
    assert fish_fast("day6/data/real_data", 80) == 352151
    assert fish_fast("day6/data/larger_cave", 256) == 26984457539
    assert fish_fast("day6/data/real_data", 256) == 1601616884019