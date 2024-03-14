def calc_max_profit(days: int, prices: list[int], fish_alive: int):

    l, r = 0, 1
    max_profit = 0

    while r < days:
        if prices[r] <= prices[l] or r - l > fish_alive:
            l = r
        else:
            max_profit = max(max_profit, prices[r] - prices[l])
        r += 1

    r -= 1
    l -= 1
    while l < r:
        if r - l <= fish_alive:
            max_profit = max(max_profit, prices[r] - prices[l])
        l += 1
    return max_profit


if __name__ == "__main__":
    days, fish_alive = map(int, input().split())
    prices = [int(price) for price in input().split()]
    res = calc_max_profit(days, prices, fish_alive)
    print(res)
