from lesson1.task_A import task_A


def test_task1():
    assert task_A(0, 7, 12, 5) == 25
    assert task_A(10, 2, -10, 2) == 10
    assert task_A(1000, 100, -1000, 100) == 402
    assert task_A(1000, 50, 1000, 50) == 101
    assert task_A(1000, 50, 1000, 51) == 103

    assert task_A(0, 5, 0, 7) == 15
    assert task_A(-100, 1, -200, 0) == 4
    assert task_A(-100, 1, -100, 0) == 3
    assert task_A(-50, 2, -60, 3) == 12
    assert task_A(-50, 10, 60, 5) == 32
    assert task_A(-50, 10, -60, 5) == 26