from lesson2.task_H import find_best_ban


def test_min_possible_section_division():
    assert find_best_ban([
        [1, 2],
        [3, 4],
    ]) == (2, 2)

    assert find_best_ban([
        [1, 3, 5, 7],
        [9, 11, 2, 4],
        [6, 8, 10, 12],
    ]) == (3, 2)

    assert find_best_ban([
        [1, 2, 1],
        [2, 1, 1],
        [2, 1, 1],
    ]) == (1, 1)

    assert find_best_ban([
        [1, 2, 1],
        [2, 1, 1],
        [3, 1, 3],
    ]) == (3, 1)

    assert find_best_ban([
        [97, 1, 2, 3, 4],
        [10, 2, 100, 1, 7],
        [3, 9, 99, 5, 10],
        [1, 7, 3, 98, 6],
    ]) == (4, 3)     # 8 simplify

    assert find_best_ban([
        [999999997, 1, 2, 3, 4],
        [10, 2, 1000000000, 1, 7],
        [3, 9, 999999999, 5, 10],
        [1, 7, 3, 999999998, 6],
    ]) == (4, 3)    # 8

    with open("H_09.txt") as fi:
        data = fi.readlines()
        n, m = map(int, data[0].split())
        table = []
        for i in range(1, n + 1):
            row = list(map(int, data[i].split()))
            table.append(row)
        res = find_best_ban(table)
        assert res == (4, 4)

    with open("H_15.txt") as fi:
        data = fi.readlines()
        n, m = map(int, data[0].split())
        table = []
        for i in range(1, n + 1):
            row = list(map(int, data[i].split()))
            table.append(row)
        res = find_best_ban(table)
        assert res
