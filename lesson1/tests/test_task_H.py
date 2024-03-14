from lesson1.task_H import calc_min_time_same_distance


def test_calc_rounds():
    assert calc_min_time_same_distance(6, 3, 1, 1, 1) == 1
    assert calc_min_time_same_distance(12, 8, 10, 5, 20) == 0.3
    assert calc_min_time_same_distance(5, 0, 0, 1, 2) == 2
    assert calc_min_time_same_distance(10, 7, -3, 1, 4) == 0.8571428571

    assert calc_min_time_same_distance(762899414, 556082848, 539099316, 556082848, 582799403) == 0 # 5
    assert calc_min_time_same_distance(615143346, 79387687, -80123649, 306422480, -80123649) == 2.4075923389 # 7
    assert calc_min_time_same_distance(948744004, 861724643, 848773505, 584154450, 730556189) == 0.2859497398  # 8
    assert calc_min_time_same_distance(72, 20, -38121735, 66, 288888467) == 0.0000000795   # 10
    assert calc_min_time_same_distance(94, 76, 0, 76, 0.0000000000) == 0   # 11
    assert calc_min_time_same_distance(956390104, 549514100, 7, 315097830, -7) == 51569559.5714285714  # 20
    assert calc_min_time_same_distance(1, 0, 0, 0, 0) == 0   # 21

