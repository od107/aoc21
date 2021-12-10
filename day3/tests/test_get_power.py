from day3.get_power import *

def test_get_power():
    assert get_power("day3/data/test_data") == 198
    assert get_power("day3/data/real_data") == 3813416

def test_life_support():
    assert life_support("day3/data/test_data") == 230
 #   assert life_support("day3/data/real_data") == 3813416