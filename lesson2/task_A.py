def calc_min_rectangle(coords: list[tuple[int, int]]):
    x_left = min(coords, key=lambda x: x[0])[0]
    y_left = min(coords, key=lambda x: x[1])[1]
    x_right = max(coords, key=lambda x: x[0])[0]
    y_right = max(coords, key=lambda x: x[1])[1]

    return " ".join(map(str, [x_left, y_left, x_right, y_right]))


if __name__ == "__main__":
    k = int(input())
    coords = []
    for _ in range(k):
        coords.append(tuple(map(int, input().split())))
    res = calc_min_rectangle(coords)
    print(res)
