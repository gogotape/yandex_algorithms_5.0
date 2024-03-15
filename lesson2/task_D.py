def calc_cut_figure_perimeter(cells: list[tuple[int, int]]):

    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]

    seen = set()

    def dfs(root_cell: tuple[int ,int]):

        if not root_cell:
            return 0

        x, y = root_cell
        seen.add(root_cell)
        perimeter_incr = 4
        neighbours = []

        for direction in directions:
            if (x + direction[0], y + direction[1]) in cells:
                neighbours.append((x + direction[0], y + direction[1]))
                perimeter_incr -= 1

        for neighbour in neighbours:
            if neighbour not in seen:
                perimeter_incr += dfs(neighbour)
                seen.add(neighbour)

        return perimeter_incr

    return dfs(root_cell=cells[0] if cells else None)


if __name__ == "__main__":
    n = int(input())
    cells = []
    for _ in range(n):
        x, y = map(int, input().split())
        cells.append((x, y))
    res = calc_cut_figure_perimeter(cells)
    print(res)
