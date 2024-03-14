def calc_min_time_same_distance(L, x1, v1, x2, v2):

    if v1 == v2 == 0 and x1 != x2 and x1 != L - x2:
        return -1
    if v1 == v2 and x1 == x2:
        return 0

    K_pos = x1
    K_speed = v1
    A_pos = x2
    A_speed = v2

    first = None
    second = None
    third = None
    fourth = None
    fifth = None
    six = None
    seven = None

    if K_speed - A_speed != 0:
        first = (A_pos - K_pos) / (K_speed - A_speed)
        fourth = (-L + A_pos - K_pos) / (K_speed - A_speed)
        fifth = (-2 * L + A_pos - K_pos) / (K_speed - A_speed)
        seven = (L + A_pos - K_pos) / (K_speed - A_speed)

    if K_speed + A_speed != 0:
        second = (L - K_pos - A_pos) / (A_speed + K_speed)
        six = (2*L - K_pos - A_pos) / (A_speed + K_speed)
        third = (- K_pos - A_pos) / (A_speed + K_speed)

    results = [
        first,
        second,
        third,
        fourth,
        fifth,
        six,
        seven,
    ]

    positive_results = [result for result in results if result is not None and result >= 0]
    output = min(positive_results) if positive_results else - 1
    return round(output, 10)


if __name__ == "__main__":
    L, x1, v1, x2, v2 = map(int, input().split())
    res = calc_min_time_same_distance(L, x1, v1, x2, v2)
    if res == -1:
        print("NO")
    else:
        print("YES")
        print(res)
