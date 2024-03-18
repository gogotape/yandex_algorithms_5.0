def calc_max_win(sectors: list[int], a: int, b: int, k: int):

    sectors_count = len(sectors)
    possible_wins = set()

    min_speed_incr = a // k if a % k != 0 else a // k - 1
    max_speed_incr = b // k if b % k != 0 else b // k - 1

    if a <= k and b <= k:
        return sectors[0]

    if max_speed_incr - min_speed_incr >= sectors_count:
        return max(sectors)

    min_speed_sector = min_speed_incr % sectors_count
    max_speed_sector = max_speed_incr % sectors_count

    if min_speed_sector == max_speed_sector and a == b:
        possible_wins.add(sectors[max_speed_sector])
        possible_wins.add(sectors[sectors_count - max_speed_sector])
        return max(possible_wins)

    # right
    if min_speed_sector > max_speed_sector:
        for i in range(min_speed_sector + 1, sectors_count):
            possible_wins.add(sectors[i])
        for i in range(max_speed_sector + 1):
            possible_wins.add(sectors[i])
    else:
        for i in range(min_speed_sector, max_speed_sector + 1):
            possible_wins.add(sectors[i])

    # left
    if sectors_count - min_speed_sector < sectors_count - max_speed_sector:
        for i in range(sectors_count - min_speed_sector + 1):
            possible_wins.add(sectors[i])
        for i in range(sectors_count - max_speed_sector, sectors_count):
            possible_wins.add(sectors[i])
    else:
        for i in range(sectors_count - max_speed_sector, sectors_count - min_speed_sector + 1):
            if i == sectors_count:
                i = 0
            possible_wins.add(sectors[i])

    return max(possible_wins)


if __name__ == "__main__":
    n = int(input())
    sectors = [int(_) for _ in input().split()]
    a, b, k = [int(_) for _ in input().split()]
    res = calc_max_win(sectors, a, b, k)
    print(res)
