def calc_max_snail_high(berries: list[tuple[int, int]]):

    positive, neutral, negative = [], [], []
    min_non_negative_jump_diff_value = -1
    min_non_negative_jump_diff_index = None
    max_jump = 0
    max_jump_ind = None
    max_negative_jump_value = 0
    max_negative_jump_index = None

    for i, berry in enumerate(berries):
        diff = berry[0] - berry[1]
        jump = berry[0]
        if jump > max_jump:
            max_jump = jump
            max_jump_ind = i

        if diff >= 0:
            positive.append(i)
            if berry[1] > min_non_negative_jump_diff_value:
                min_non_negative_jump_diff_value = berry[1]
                min_non_negative_jump_diff_index = i
        else:
            negative.append(i)
            if jump > max_negative_jump_value:
                max_negative_jump_value = jump
                max_negative_jump_index = i

    if not positive:
        return max_jump, [max_jump_ind + 1] + [neg + 1 for neg in negative if
                                               neg != max_jump_ind]

    all_non_negative = sum(berries[i][0] - berries[i][1] for i in (positive + neutral))
    last_non_negative = all_non_negative + berries[min_non_negative_jump_diff_index][1]

    if max_negative_jump_index:
        last_negative = all_non_negative + berries[max_negative_jump_index][0]
    else:
        last_negative = -1

    if last_negative > last_non_negative:
        max_high = last_negative
        arr = [pos + 1 for pos in positive] + [max_negative_jump_index + 1] + [neg + 1 for neg in negative if neg != max_negative_jump_index]
    else:
        max_high = last_non_negative
        arr = [pos + 1 for pos in positive if pos != min_non_negative_jump_diff_index] + [min_non_negative_jump_diff_index + 1] + [neg + 1 for neg in negative]

    return max_high, arr


if __name__ == "__main__":
    n = int(input())
    berries = []
    for _ in range(n):
        up, down = map(int, input().split())
        berries.append((up, down))
    res = calc_max_snail_high(berries)
    print(res[0])
    print(" ".join(str(elem) for elem in res[1]))
