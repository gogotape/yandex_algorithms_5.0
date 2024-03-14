def beat_by_figure(coords, figure_type: str, input_data, board):

    x, y = coords

    def __check_index(indx):
        return 0 <= indx <= 7

    def __is_empty(x, y):
        return input_data[x][y] not in ("B", "R")

    directions = []
    if figure_type == "B":
        directions = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    elif figure_type == "R":
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    for x_delta, y_delta in directions:
        temp_x, temp_y = x, y
        while __check_index(temp_x) and __check_index(temp_y):
            if temp_y == y and temp_x == x or __is_empty(temp_x, temp_y):
                board[temp_x][temp_y] = 1
                temp_x += x_delta
                temp_y += y_delta
            else:
                break


def main(input_data):
    rocks, bishops = [], []
    board = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if input_data[i][j] == "R":
                rocks.append((i, j))
            elif input_data[i][j] == "B":
                bishops.append((i, j))

    for rock in rocks:
        beat_by_figure(rock, "R", input_data, board)
    for bishop in bishops:
        beat_by_figure(bishop, "B", input_data, board)

    summ = sum(sum(row) for row in board)
    res = 64 - summ
    return res


if __name__ == "__main__":
    input_data = [[item for item in input()[:8]] for _ in range(8)]
    print(main(input_data))
