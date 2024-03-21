from lesson3.task_A import find_common_tracks


def test_find_common_tracks():
    assert find_common_tracks([["GoGetIt", "Life"]]) == ["GoGetIt", "Life"]
    assert find_common_tracks([["Love", "Life"], ["Life", "GoodDay"]]) == ["Life"]
