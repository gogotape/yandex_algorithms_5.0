import math


def solve_eq(n):
    a = 1
    b = -1
    c = 2 - 2 * n

    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return int(x1) if x1 > 0 else int(x2)
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        raise ValueError


def sum_prog(n):
    return (1 + n) * n // 2


def find_fraction(n):

    l, r = 0, n + 1

    while l < r:
        mid = (r + l) // 2
        if sum_prog(mid) >= n:
            r = mid
        else:
            l = mid + 1

    number_of_d = l

    shift = n - sum_prog(number_of_d - 1)

    if number_of_d % 2 == 0:
        up = number_of_d - shift + 1
        down = shift
    else:
        up = shift
        down = number_of_d - shift + 1

    return int(up), int(down)


if __name__ == '__main__':
    n = int(input())
    res = find_fraction(n)
    up, down = res
    print(str(up)+"/"+str(down))
