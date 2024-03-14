from lesson1.task_F import main


def test_main():
    assert main([5, 7, 2]) == "x+"
    assert main([4, -5]) == "+"
    assert main([2, 2, 2, 3]) == "+++"
    assert main([2, 3]) == "+"
    assert main([7, 7]) == "x"
