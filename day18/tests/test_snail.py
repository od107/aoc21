from day18.snailfish import *


def test_explode():
    assert explode('[[[[[9,8],1],2],3],4]')[0] == '[[[[0,9],2],3],4]'
    assert explode('[7,[6,[5,[4,[3,2]]]]]')[0] == '[7,[6,[5,[7,0]]]]'
    assert explode('[[6,[5,[4,[3,2]]]],1]')[0] == '[[6,[5,[7,0]]],3]'
    assert explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')[0] == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    assert explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')[0] == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'


# def test_split():
#     assert split('[[[[0,7],4],[15,[0,13]]],[1,1]]') == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
#     assert split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]') == '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'


def test_add():
    assert add("day18/data/test_data1") == '[[[[1,1],[2,2]],[3,3]],[4,4]]'
    assert add("day18/data/test_data2") == '[[[[3,0],[5,3]],[4,4]],[5,5]]'
    assert add("day18/data/test_data3") == '[[[[5,0],[7,4]],[5,5]],[6,6]]'
    # assert add("day18/data/test_data4") == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
    # assert add("day18/data/test_data5") == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'


# def test_magnitude():
#     assert magnitude('[[1,2],[[3,4],5]]') == 143
#     assert magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]') == 1384
#     assert magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]') == 445
#     assert magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]') == 791
#     assert magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]') == 1137
#     assert magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]') == 1137
#     assert magnitude('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]') == 4140



