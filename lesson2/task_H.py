def find_best_ban(table: list[list[int]]):

    rows, columns = len(table), len(table[0])

    max_elem_val = 0
    max_elem = (0, 0)

    for i, row in enumerate(table):
        for j, val in enumerate(row):
            if val > max_elem_val:
                max_elem = i, j
                max_elem_val = val

    matrix_without_row = [table[r] for r in range(rows) if r != max_elem[0]]
    matrix_without_column = [[table[r][c] for c in range(columns) if c != max_elem[1]] for r in range(rows)]

    max_elem_matrix_without_row_val = 0
    max_elem_matrix_without_row = (0, 0)
    for i, row in enumerate(matrix_without_row):
        for j, val in enumerate(row):
            if val > max_elem_matrix_without_row_val:
                max_elem_matrix_without_row_val = val
                max_elem_matrix_without_row = i, j
    matrix1 = [[matrix_without_row[r][c] for c in range(columns) if c != max_elem_matrix_without_row[1]] for r in range(rows - 1)]

    max_elem_matrix_without_column_val = 0
    max_elem_matrix_without_column = (0, 0)
    for i, row in enumerate(matrix_without_column):
        for j, val in enumerate(row):
            if val > max_elem_matrix_without_column_val:
                max_elem_matrix_without_column_val = val
                max_elem_matrix_without_column = i, j
    matrix2 = [matrix_without_column[r] for r in range(rows) if r != max_elem_matrix_without_column[0]]

    max_elem_matrix_without_row_and_column = 0
    max_elem_matrix_without_column_and_row = 0

    for i, row in enumerate(matrix1):
        for j, val in enumerate(row):
            if val > max_elem_matrix_without_row_and_column:
                max_elem_matrix_without_row_and_column = val

    for i, row in enumerate(matrix2):
        for j, val in enumerate(row):
            if val > max_elem_matrix_without_column_and_row:
                max_elem_matrix_without_column_and_row = val

    if max_elem_matrix_without_row_and_column < max_elem_matrix_without_column_and_row or (max_elem_matrix_without_row_and_column == max_elem_matrix_without_column_and_row and max_elem_matrix_without_row_val > max_elem_matrix_without_column_val):
        max_res_val = max_elem[0], max_elem_matrix_without_row[1]
    else:
        max_res_val = max_elem_matrix_without_column[0], max_elem[1]

    return max_res_val[0] + 1, max_res_val[1] + 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        row = list(map(int, input().split()))
        table.append(row)
    res = find_best_ban(table)
    print(" ".join([str(i) for i in res]))
