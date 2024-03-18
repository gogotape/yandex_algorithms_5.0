from lesson2.task_G import calc_min_possible_section_division


def test_min_possible_section_division():
    assert calc_min_possible_section_division([1, 3, 3, 3, 2])[0] == 3
    assert calc_min_possible_section_division([1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9])[0] == 3
    assert calc_min_possible_section_division([7, 2, 3, 4, 3, 2, 7])[0] == 3

    assert calc_min_possible_section_division([1, 1, 1, 1, 1, 1, 1])[0] == 7
    assert calc_min_possible_section_division([1, 2, 1, 1, 1, 1, 1])[0] == 7
    assert calc_min_possible_section_division([1, 2, 3, 1, 1, 1, 1])[0] == 6

    assert calc_min_possible_section_division([1, 1, 9, 2, 9, 9, 9, 5, 8])[0] == 4
    assert calc_min_possible_section_division([10, 9, 9, 10, 3, 4, 1, 8, 2, 7])[0] == 5
    assert calc_min_possible_section_division([10, 10, 10, 1, 5, 8, 4, 8, 9, 8])[0] == 4
    assert calc_min_possible_section_division([1, 3, 10, 4, 6, 4, 3, 7, 6, 10])[0] == 4
