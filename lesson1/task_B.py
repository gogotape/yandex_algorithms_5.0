def task_B(m1g1, m1g2, m2g1, m2g2, home):

    t1 = m1g1 + m2g1
    t2 = m1g2 + m2g2

    if t1 > t2:
        return 0

    if t1 <= t2:
        to_draw = t2 - t1
        if home == 2:
            guest_goals_t1 = m1g1
            guest_goals_t2 = m2g2
        elif home == 1:
            guest_goals_t1 = m2g1 + to_draw
            guest_goals_t2 = m1g2

        if guest_goals_t1 > guest_goals_t2:
            return to_draw
        else:
            return to_draw + 1
