from lesson3.task_F import replace_words


def test_replace_words():
    assert replace_words(
        ["a", "b"],
        ["abdafb", "basrt", "casds", "dsasa", "a"]
    ) == ["a", "b", "casds", "dsasa", "a"]

    assert replace_words(
        ["aa", "bc", "aaa"],
        ["a", "aa", "aaa", "bcd", "abcd"]
    ) == ["a", "aa", "aa", "bc", "abcd"]
