def calc_min_len_of_rope(pieces: list):

    total = 0
    maxx = 0

    for piece in pieces:
        total += piece
        maxx = max(maxx, piece)

    if (total - maxx) < maxx:
        return maxx - (total - maxx)
    else:
        return total


if __name__ == "__main__":
    N = int, input().split()
    pieces = [int(piece) for piece in input().split()]
    res = calc_min_len_of_rope(pieces)
    print(res)
