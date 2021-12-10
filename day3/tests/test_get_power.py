from day3.get_power import *

def test_get_power():
    assert get_power("day3/data/test_data") == 198
    assert get_power("day3/data/real_data") == 3813416