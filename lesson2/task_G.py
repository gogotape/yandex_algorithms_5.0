def calc_min_possible_section_division(numbers: list[int]):
    arr = []
    l, r = 0, 0
    change_sector = 0
    while r < len(numbers):
        cur_cnt = 1
        cur_min = numbers[l]
        while r < len(numbers):
            if min(cur_min, numbers[r]) >= cur_cnt:
                cur_min = min(cur_min, numbers[r])
                cur_cnt += 1
                r += 1
            else:
                break
        arr.append(cur_cnt - 1)
        change_sector += 1
        l = r
        continue

    return change_sector, arr


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = list(map(int, input().split()))
        res = calc_min_possible_section_division(numbers)
        print(res[0])
        print(" ".join([str(i) for i in res[1]]))
