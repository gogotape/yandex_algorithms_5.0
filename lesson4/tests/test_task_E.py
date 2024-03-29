from lesson4.task_E import find_fraction


def test_find_fraction():
    assert find_fraction(1) == (1, 1)
    assert find_fraction(2) == (2, 1)
    assert find_fraction(6) == (3, 1)
