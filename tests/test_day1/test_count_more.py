from day1.count_more import count_more, count_avg

def test_count_more():
    assert count_more("data/testdata_day1") == 7

def test_count_avg():
    assert count_avg("data/testdata_day1") == 5