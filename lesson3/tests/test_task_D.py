from lesson3.task_D import is_some_values_repeating


def test_is_some_values_repeating():
    assert is_some_values_repeating([1, 2, 3, 1]) == "NO"
    assert is_some_values_repeating([1, 0, 1, 1]) == "YES"
