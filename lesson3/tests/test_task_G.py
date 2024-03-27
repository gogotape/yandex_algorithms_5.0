from lesson3.task_G import build_square


def test_build_square():
    assert build_square([(0, 1), (1, 0)])[0] == 2
    assert build_square([(0, 2), (2, 0), (2, 2)])[0] == 1
    assert build_square([(-1, 1), (1, 1), (-1, -1), (1, -1)])[0] == 0
    assert build_square([(-1, 1)])[0] == 3
