from day6.fish import *


def test_fish():
    assert fish("day6/data/test_data", 18) == 26
    assert fish("day6/data/test_data", 80) == 5934
    assert fish("day6/data/real_data", 80) == 352151


#def test_vent_diag():
#    assert vents("day6/data/test_data", False) == 12
#    assert vents("day6/data/real_data", False) == 21406