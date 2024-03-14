from lesson1.task_G import calc_rounds


def test_calc_rounds():
    assert calc_rounds(10, 11, 15) == 4
    assert calc_rounds(1, 2, 1) == -1
    assert calc_rounds(1, 1, 1) == 1
    assert calc_rounds(25, 200, 10) == 13

    assert calc_rounds(250, 500, 187) == 4
    assert calc_rounds(250, 500, 188) == 5
    assert calc_rounds(250, 500, 190) == 5

    assert calc_rounds(250, 500, 230) == 8
    assert calc_rounds(250, 500, 208) == 5
    assert calc_rounds(250, 500, 249) == 101 # 39
    assert calc_rounds(250, 500, 218) == 6    # 13
