def calc_min_moves(n: int, ships: list[tuple[int, int]]) -> int:

    ships = list(sorted(ships, key=lambda x: x[0]))

    sort_to_diff_rows = 0
    new_ships = []
    for i, ship in enumerate(ships, start=1):
        x, y = ship
        sort_to_diff_rows += abs(x - i)
        new_ships.append((i, y))

    possible_solutions = []
    for column in range(1, n + 1):
        solution = 0
        for ship in new_ships:
            x, y = ship
            solution += abs(y - column)

        solution += sort_to_diff_rows
        possible_solutions.append(solution)

    return min(possible_solutions)


if __name__ == "__main__":
    n = int(input())
    ships = []
    for _ in range(n):
        x, y = map(int, input().split())
        ship = tuple((x, y))
        ships.append(ship)
    res = calc_min_moves(n, ships)
    print(res)
