from lesson1.task_B import task_B


def test_task2():
    assert task_B(0, 0, 0, 0, 1) == 1
    assert task_B(0, 2, 0, 3, 1) == 5
    assert task_B(0, 2, 0, 3, 2) == 6

    assert task_B(5, 0, 5, 0, 1) == 0
    assert task_B(5, 0, 5, 0, 2) == 0
    assert task_B(0, 5, 0, 5, 1) == 10
    assert task_B(0, 5, 0, 5, 2) == 11
    assert task_B(0, 2, 2, 0, 1) == 1
    assert task_B(0, 2, 2, 0, 2) == 1
    assert task_B(0, 3, 3, 2, 1) == 2
    assert task_B(0, 3, 3, 2, 2) == 3
    assert task_B(0, 0, 0, 0, 2) == 1
    assert task_B(1, 1, 2, 2, 1) == 0
    assert task_B(1, 1, 2, 2, 2) == 1
