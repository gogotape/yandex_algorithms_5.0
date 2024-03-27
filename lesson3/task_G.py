def find_two_others(xA, yA, xC, yC):
    """
    find points coordinates from other diagonal
    """
    dy = yA - yC
    dx = xC - xA
    d = (dx - dy) / 2
    xD = xA + d
    yD = yC - d
    xB = xC - d
    yB = yA + d
    return xB, yB, xD, yD


def build_square(points: list[tuple[int, int]]) -> (int, tuple[int, int]):

    st = set(points)

    if len(points) == 1:
        xA, yA = points[0]
        xC, yC = xA + 1, yA + 1
        xB, yB, xD, yD = find_two_others(xA, yA, xC, yC)
        return 3, [(xC, yC), (xB, yB), (xD, yD)]

    min_to_build = 2
    min_to_build_points = []

    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points[i + 1:]):
            xA, yA = point1
            xC, yC = point2
            xB, yB, xD, yD = find_two_others(xA, yA, xC, yC)
            if (xB, yB) in st and (xD, yD) in st:
                return 0, []
            elif (xB, yB) in st:
                min_to_build = 1
                min_to_build_points = [(xD, yD)]
            elif (xD, yD) in st:
                min_to_build = 1
                min_to_build_points = [(xB, yB)]

    if min_to_build == 1 and min_to_build_points:
        return min_to_build, min_to_build_points

    xA, yA = points[0]
    xC, yC = xA + 1, yA + 1
    xB, yB, xD, yD = find_two_others(xA, yA, xC, yC)

    return 2, [(xB, yB), (xD, yD)]


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        tp = tuple(map(int, input().split()))
        points.append(tp)
    res = build_square(points)
    n_points, new_points = res
    print(n_points)
    if res:
        for i in range(n_points):
            print(*points[i])
