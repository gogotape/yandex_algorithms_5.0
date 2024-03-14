from lesson1.task_I import choose_days


def test_task7():
    assert choose_days(2013, {(6, "February"), (13, "February"), (20, "February")}, "Tuesday") == "Tuesday Wednesday"   # 3
    assert choose_days(2015, {(1, "January"), (8, "January")}, "Thursday")  # any "Monday Tuesday"

    with open("34.txt") as fi:
        data = fi.readlines()
        n = int(data[0])
        year = int(data[1])
        holidays = set()
        for i in range(2, n + 2):
            day, month = data[i].split()
            holidays.add((int(day), month))
        first_day_of_week = data[-1]

    assert choose_days(year, holidays, first_day_of_week) == "Monday Tuesday" # 34
