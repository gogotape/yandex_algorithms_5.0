from lesson2.task_A import calc_min_rectangle


def test_task_A():
    assert calc_min_rectangle([(1, 3), (3, 1), (3, 5), (6, 3)]) == "1 1 6 5"
