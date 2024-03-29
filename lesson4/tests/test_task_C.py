from lesson4.task_C import (find_number_of_start_regiment_for_sortie,
                            calc_prefix_sum, calc_sum_between_two_index,
                            l_bin_search)


def test_calc_prefix_sum():
    assert calc_prefix_sum([1, 3, 5, 7, 9]) == [1, 4, 9, 16, 25]
    assert calc_prefix_sum([10, 4, 16, 20]) == [10, 14, 30, 50]
    assert calc_prefix_sum([3, 6, 2, 8, 9, 2]) == [3, 9, 11, 19, 28, 30]


def test_calc_sum_between_two_index():
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 0, 0) == 3
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 4, 5) == 11
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 3, 5) == 19
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 0, 5) == 30
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 0, 1) == 9
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 1, 3) == 16
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 2, 3) == 10
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 2, 5) == 21
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 3, 3) == 8
    assert calc_sum_between_two_index([3, 9, 11, 19, 28, 30], 1, 1) == 6
    assert calc_sum_between_two_index([3, 9], 0, 0) == 3
    assert calc_sum_between_two_index([3, 9], 0, 1) == 9
    assert calc_sum_between_two_index([3, 9], 1, 1) == 6


def test_l_bin_search():
    ps = [3, 9]
    assert l_bin_search(ps, 1, 3) == 0
    assert l_bin_search(ps, 1, 6) == 1
    assert l_bin_search(ps, 2, 9) == 0
    assert l_bin_search(ps, 2, 10) == -1
    assert l_bin_search(ps, 2, 8) == -1


def test_find_number_of_start_regiment_for_sortie():
    prefix_sum = calc_prefix_sum([1, 3, 5, 7, 9])
    assert find_number_of_start_regiment_for_sortie(prefix_sum, 2, 4) == 1
    assert find_number_of_start_regiment_for_sortie(prefix_sum, 1, 3) == 2

    #   2
    prefix_sum = calc_prefix_sum([570703232, 570703232, 570703232, 570703232, 570703232])
    assert find_number_of_start_regiment_for_sortie(prefix_sum, 2, 687772523) == -1
    assert find_number_of_start_regiment_for_sortie(prefix_sum, 1, 570703232) == 3
    assert find_number_of_start_regiment_for_sortie(prefix_sum, 2, 1141406464) == 3
    assert find_number_of_start_regiment_for_sortie(prefix_sum, 3, 1712109696) == 3

    #   3
    with open("test_data_C/C_03.txt") as f:
        data = f.readlines()

    _, m = map(int, data[0].split())
    regiments = list(map(int, data[1].split()))

    prefix_sum = calc_prefix_sum(regiments)

    for i in range(2, m + 2):
        regiment_count, orcs_count = map(int, data[i].split())
        res = find_number_of_start_regiment_for_sortie(
            prefix_sum,
            regiment_count,
            orcs_count
        )


    #   5
    with open("test_data_C/C_05.txt") as f:
        data = f.readlines()

    _, m = map(int, data[0].split())
    regiments = list(map(int, data[1].split()))
    prefix_sum = calc_prefix_sum(regiments)

    for i in range(2, m + 2):
        regiment_count, orcs_count = map(int, data[i].split())
        res = find_number_of_start_regiment_for_sortie(
            prefix_sum,
            regiment_count,
            orcs_count
        )


    #   6
    with open("test_data_C/C_06.txt") as f:
        data = f.readlines()

    _, m = map(int, data[0].split())
    regiments = list(map(int, data[1].split()))

    prefix_sum = calc_prefix_sum(regiments)
    for i in range(2, m + 2):
        regiment_count, orcs_count = map(int, data[i].split())
        res = find_number_of_start_regiment_for_sortie(
            prefix_sum,
            regiment_count,
            orcs_count
        )

    #   7
    with open("test_data_C/C_07.txt") as f:
        data = f.readlines()

    _, m = map(int, data[0].split())
    regiments = list(map(int, data[1].split()))
    prefix_sum = calc_prefix_sum(regiments)

    with open("test_data_C/C_07a.txt") as f:
        answers = list(map(int, f.readline().split()))

    for i in range(2, m + 2):
        regiment_count, orcs_count = map(int, data[i].split())
        res = find_number_of_start_regiment_for_sortie(
            prefix_sum,
            regiment_count,
            orcs_count
        )
        assert res == answers[i - 2]
