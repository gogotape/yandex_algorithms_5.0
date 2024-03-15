from lesson2.task_D import calc_cut_figure_perimeter


def test_calc_cut_figure_perimeter():
    assert calc_cut_figure_perimeter([(1, 1), (1, 2), (2, 1)]) == 8
    assert calc_cut_figure_perimeter([(8, 8)]) == 4
