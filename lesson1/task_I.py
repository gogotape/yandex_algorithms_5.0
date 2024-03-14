def choose_days(year: int, holidays: set[tuple], first_day_of_week: str) -> [str, str]:

    if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
        days_in_year = 366
    else:
        days_in_year = 365

    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    months = {
        1: ("January", 31),
        2: ("February", 28 if days_in_year == 365 else 29),
        3: ("March", 31),
        4: ("April", 30),
        5: ("May", 31),
        6: ("June", 30),
        7: ("July", 31),
        8: ("August", 31),
        9: ("September", 30),
        10: ("October", 31),
        11: ("November", 30),
        12: ("December", 31),
    }

    hm = {day_of_week: 0 for day_of_week in days_of_week}

    cur_month = 1
    cur_day = 1
    cur_week_day = 1
    cur_month_day = 1
    cur_month_days = months.get(cur_month)[-1]
    for i, day_name in days_of_week.items():
        if day_name == first_day_of_week:
            cur_week_day = i

    while cur_day <= days_in_year:
        if cur_month_day > cur_month_days:
            cur_month += 1
            cur_month_days = months.get(cur_month)[-1]
            cur_month_day = 1

        if cur_week_day == 8:
            cur_week_day = 1

        cur_month_name = months.get(cur_month)[0]

        if (cur_month_day, cur_month_name) in holidays:
            for week_day in hm:
                hm[week_day] += 1
        else:
            hm[cur_week_day] += 1

        cur_day += 1
        cur_month_day += 1
        cur_week_day += 1

    hm = list(sorted(hm.items(), key=lambda x: x[1]))
    best = days_of_week.get(hm[-1][0])
    worst = days_of_week.get(hm[0][0])

    return best + " " + worst


if __name__ == "__main__":
    n = int(input())
    year = int(input())
    holidays = set()
    for _ in range(n):
        day, month = input().split()
        holidays.add((int(day), month))
    first_day_of_week = input()
    res = choose_days(
        year=year,
        holidays=holidays,
        first_day_of_week=first_day_of_week,
    )

    print(res)
