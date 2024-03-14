from lesson2.task_B import calc_max_profit


def test_calc_max_profit():
    assert calc_max_profit(5, [1, 2, 3, 4, 5], 2) == 2
    assert calc_max_profit(5, [5, 4, 3, 2, 1], 2) == 0
    assert calc_max_profit(3, [1, 2, 4], 1) == 2 # 5
    assert calc_max_profit(4, [2, 2, 4, 5], 2) == 3  # 8
