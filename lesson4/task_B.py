def find_max_size_of_ship(n: int) -> int:
    km = int((n * 6) ** (1 / 3))
    for k in range(km, 0 - 1, -1):
        if n * 6 >= k ** 3 + 9 * k ** 2 + 20 * k + 6:
            return k + 1
    return 0


if __name__ == '__main__':
    n = int(input())
    res = find_max_size_of_ship(n)
    print(res)
