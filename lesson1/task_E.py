def calc_profit(n, k, days):
    profit = n
    for _ in range(days):
        profit = profit * 10
        for digit in range(0, 10):
            if (profit + digit) % k == 0:
                profit += digit
                if digit == 0:
                    res = str(profit)
                    for day in range(_ + 1, days):
                        res += str(0)
                    try:
                        return int(res)
                    except ValueError:
                        return res
                break

        else:
            return -1

    return profit


if __name__ == "__main__":
    n, k, days = map(int, input().split())
    print(calc_profit(n, k, days))
