from lesson3.task_I import play_football


data_dir = "task_I_data"


def test_play_football():
    with open(f"{data_dir}/1.txt") as f:
        data = f.readlines()
    assert play_football(data) == [3, 0, 1.0, 0.5, 1.0, 0]

    with open(f"{data_dir}/custom_test.txt") as f:
        data = f.readlines()
    assert play_football(data)

    with open(f"{data_dir}/3.txt") as f:    # 3
        data = f.readlines()
    assert play_football(data)
