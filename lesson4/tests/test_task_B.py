from lesson4.task_B import find_max_size_of_ship


def test_find_max_size_of_ship():
    assert find_max_size_of_ship(7) == 2
    assert find_max_size_of_ship(6) == 2
    assert find_max_size_of_ship(0) == 0
    assert find_max_size_of_ship(1) == 1



