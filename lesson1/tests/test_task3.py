from lesson1.task_C import fix_row, fix_file


def test_task3_fix_row():
    assert fix_row(1) == 1
    assert fix_row(4) == 1
    assert fix_row(12) == 3
    assert fix_row(9) == 3
    assert fix_row(0) == 0
    assert fix_row(5) == 2
    assert fix_row(6) == 3
    assert fix_row(7) == 3
    assert fix_row(8) == 2

    assert fix_row(10) == 4
    assert fix_row(11) == 4
    assert fix_row(100) == 25
    assert fix_row(13) == 4
    assert fix_row(14) == 5
    assert fix_row(15) == 5
    assert fix_row(16) == 4
    assert fix_row(17) == 5
    assert fix_row(18) == 6


def test_task3_fix_file():
    assert fix_file(lst=[1, 4, 12, 9, 0]) == 8
    assert fix_file(lst=[1]) == 1
    assert fix_file([2]) == 2
    assert fix_file([3]) == 2
    assert fix_file([4]) == 1
    assert fix_file([1, 15, 2, 0, 0, 30, 40]) == 1 + 5 + 2 + 9 + 10
