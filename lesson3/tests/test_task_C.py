from lesson3.task_C import find_min_numbers_amount_to_delete


def test_find_min_numbers_amount_to_delete():
    assert find_min_numbers_amount_to_delete([1, 2, 3, 4, 5]) == 3
    assert find_min_numbers_amount_to_delete([1, 1, 2, 3, 5, 5, 2, 2, 1, 5]) == 4
