from lesson2.task_F import calc_max_win


def test_calc_max_win():
    assert calc_max_win([1, 2, 3, 4, 5], 3, 5, 2) == 5
    assert calc_max_win([1, 2, 3, 4, 5], 15, 15, 2) == 4
    assert calc_max_win([5, 4, 3, 2, 1], 2, 5, 2) == 5
    assert calc_max_win([692, 407, 437, 713, 964, 10], 49, 79, 384) == 692 # 4
    assert calc_max_win([707, 805, 279, 713, 584, 352, 923, 1000, 237], 29, 38, 1) == 1000 # 5

    assert calc_max_win([925, 160, 322, 433, 698, 458, 923, 877, 741], 46, 92, 12) == 923 # 9
