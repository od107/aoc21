from day1.count_more import count_more, count_avg

def test_count_more():
    assert count_more("day1/data/testdata_day1") == 7
    assert count_more("day1/data/real_data_day1") == 1448

def test_count_avg():
    assert count_avg("day1/data/testdata_day1") == 5
    assert count_avg("day1/data/real_data_day1") == 1471
