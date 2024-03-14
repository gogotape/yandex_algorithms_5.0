def fix_row(need: int) -> int:
    tab = need // 4
    spaces = need % 4
    if spaces == 3:
        spaces = 2
    return tab + spaces


def fix_file(lst: list):
    res = [fix_row(item) for item in lst]
    return sum(res)


if __name__ == "__main__":
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    print(fix_file(lst))
