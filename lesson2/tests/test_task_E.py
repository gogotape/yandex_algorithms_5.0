from lesson2.task_E import calc_max_snail_high


def test_calc_max_snail_high():
    assert calc_max_snail_high([(1, 5), (8, 2), (4, 4)])[0] == 10
    assert calc_max_snail_high([(7, 6), (7, 4)])[0] == 10

    with open("E_4.txt") as fi:
        data = fi.readlines()
        n = int(data[0])

        berries = []
        for i in range(1, n + 1):
            x, y = data[i].split()
            berries.append((int(x), int(y)))

    assert calc_max_snail_high(berries) == (1503796355, [2, 4, 7, 5, 1, 3, 6]) # 4

    with open("E_5.txt") as fi:
        data = fi.readlines()
        n = int(data[0])

        berries = []
        for i in range(1, n + 1):
            x, y = data[i].split()
            berries.append((int(x), int(y)))

    assert calc_max_snail_high(berries)[0] == 1358752213 #, [1, 5, 4, 2, 3]) # 5

    assert calc_max_snail_high([
        (822889311, 446755913),
        (715477619, 181424399),
        (61020590, 573085537),
        (480845266, 448565595),
        (135599877, 389312924),
        (160714711, 449656269)])[0] == 1391031884   # 7

    with open("E_16.txt") as fi:
        data = fi.readlines()
        n = int(data[0])

        berries = []
        for i in range(1, n + 1):
            x, y = data[i].split()
            berries.append((int(x), int(y)))

    assert calc_max_snail_high(berries)[0] == 277086265512  # 16

    with open("E_33.txt") as fi:
        data = fi.readlines()
        n = int(data[0])

        berries = []
        for i in range(1, n + 1):
            x, y = data[i].split()
            berries.append((int(x), int(y)))

    assert calc_max_snail_high(berries) # 33
