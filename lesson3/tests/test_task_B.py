from lesson3.task_B import is_anagram


def test_is_anagram():
    assert is_anagram("dusty", "study") == "YES"
    assert is_anagram("rat", "bat") == "NO"
