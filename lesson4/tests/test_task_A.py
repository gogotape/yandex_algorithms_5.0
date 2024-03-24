from lesson4.task_A import how_much_numbers_between


def test_how_much_numbers_between():
    # 1
    assert how_much_numbers_between([1, 3, 4, 10, 10], 1, 10) == 5
    assert how_much_numbers_between([1, 3, 4, 10, 10], 2, 9) == 2
    assert how_much_numbers_between([1, 3, 4, 10, 10], 3, 4) == 2
    assert how_much_numbers_between([1, 3, 4, 10, 10], 2, 2) == 0

    # 2
    assert how_much_numbers_between([1], 1, 1) == 1
    assert how_much_numbers_between([1], -1000000000, 1000000000) == 1
    assert how_much_numbers_between([1], 1000000000, 1000000000) == 0

    # 3
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -1000000000, -1000000000) == 1
    assert how_much_numbers_between([-1000000000, 0, 1000000000], 1000000000, 1000000000) == 1
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -1000000000, 1000000000) == 3
    assert how_much_numbers_between([-100, 0, 100], -99, 99) == 1
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -999999999, 999999999) == 1
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -999999999, 1000000000) == 2
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -1000000000, 999999999) == 2
    assert how_much_numbers_between([-1000000000, 0, 1000000000], 0, 999999999) == 1
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -1, 999999999) == 1
    assert how_much_numbers_between([-1000000000, 0, 1000000000], 1, 999999999) == 0
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -999999999, -1) == 0
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -999999999, 0) == 1
    assert how_much_numbers_between([-1000000000, 0, 1000000000], -999999999, 1) == 1

    # 13
    with open("013.txt") as f:
        data = f.readlines()

    _ = int(data[0])
    arr = list(map(int, data[1].split()))
    k = int(data[2])
    arr = sorted(arr)
    results = []
    for i in range(3, k):
        left, right = map(int, data[i].split())
        res = how_much_numbers_between(arr, left, right, i)
        results.append(res)
    assert True
