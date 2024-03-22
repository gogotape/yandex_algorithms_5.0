from lesson3.task_E import find_at_least_in_two_list_numbers


def test_find_at_least_in_two_list_numbers():
    assert find_at_least_in_two_list_numbers(
        [3, 1],
        [1, 3],
        [1, 2],
    ) == [1, 3]

    assert find_at_least_in_two_list_numbers(
        [1, 2, 2],
        [3, 4, 3],
        [5],
    ) == []

    assert find_at_least_in_two_list_numbers(
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5, 6],
    ) == [2, 3, 4]

    assert find_at_least_in_two_list_numbers(
        [14, 1, 7, 16, 1, 8, 5, 13, 17, 3],
        [19, 17, 11, 2, 9],
        [9, 18, 3, 1, 9, 14],
    ) == [1, 3, 9, 14, 17]
