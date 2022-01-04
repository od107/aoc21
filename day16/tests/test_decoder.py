from day16.decoder import *


def test_part1():
    assert decode("day16/data/test_data")[0] == 16
    assert decode("day16/data/test_data_2")[0] == 12
    assert decode("day16/data/test_data_3")[0] == 23
    assert decode("day16/data/test_data_4")[0] == 31
    assert decode("day16/data/real_data")[0] == 979


def test_part2():
    assert decode(False, "C200B40A82")[1] == 3
    assert decode(False, "04005AC33890")[1] == 54
    assert decode(False, "880086C3E88112")[1] == 7
    assert decode(False, "CE00C43D881120")[1] == 9
    assert decode(False, "D8005AC2A8F0")[1] == 1
    assert decode(False, "F600BC2D8F")[1] == 0
    assert decode(False, "9C005AC2F8F0")[1] == 0
    assert decode(False, "9C0141080250320F1802104A08")[1] == 1
    assert decode("day16/data/real_data")[1] == 277110354175

