from day7.crabs import *


def test_crabs():
    assert crabs("day7/data/test_data") == 37
    assert crabs("day7/data/real_data") == 356179


#def test_fish_fast():
#    assert fish_fast("day6/data/test_data", 18) == 26
#    assert fish_fast("day6/data/test_data", 80) == 5934
#    assert fish_fast("day6/data/real_data", 80) == 352151
#    assert fish_fast("day6/data/test_data", 256) == 26984457539
#    assert fish_fast("day6/data/real_data", 256) == 1601616884019