from lesson2.task_C import calc_min_len_of_rope


def test_calc_min_len_of_rope():
    assert calc_min_len_of_rope([1, 5, 2, 1]) == 1
    assert calc_min_len_of_rope([5, 12, 4, 3]) == 24
