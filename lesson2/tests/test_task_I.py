from lesson2.task_I import calc_min_moves


def test_calc_min_moves():
    assert calc_min_moves(3, [
        (1, 2),
        (3, 3),
        (1, 1),
    ]) == 3

    assert calc_min_moves(3, [
        (1, 3),
        (1, 2),
        (1, 1),
    ]) == 5

    assert calc_min_moves(3, [
        (1, 1),
        (2, 1),
        (3, 1),
    ]) == 0

    assert calc_min_moves(3, [
        (1, 1),
        (1, 2),
        (3, 3),
    ]) == 3

    assert calc_min_moves(3, [
        (1, 1),
        (1, 2),
        (1, 3),
    ]) == 5
