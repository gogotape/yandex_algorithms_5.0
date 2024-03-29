def l_bin_search(arr, n, target_sum) -> int:
    ln = len(arr)
    l, r = 0, ln - 1

    cnt = 0
    while l <= r:
        mid = (r + l) // 2
        cnt += 1
        if cnt == 30:
            return - 1
        if mid + n > ln:
            r = mid
            continue

        cur_sum = calc_sum_between_two_index(arr, mid, mid + n - 1)
        if cur_sum == target_sum:
            return mid
        elif cur_sum > target_sum:
            r = mid
        else:
            l = mid + 1

    return -1


def find_number_of_start_regiment_for_sortie(
        prefix_sum: list[int],
        numbers_of_regiments: int,
        target_sum: int,
) -> int:

    res = l_bin_search(
        arr=prefix_sum,
        n=numbers_of_regiments,
        target_sum=target_sum
    )

    if res == -1:
        return res
    else:
        return res + 1


def calc_prefix_sum(arr: list[int]) -> list[int]:
    ln = len(arr)
    prefix_sum = [0 for _ in range(ln)]
    prefix_sum[0] = arr[0]

    for i in range(1, ln):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    return prefix_sum


def calc_sum_between_two_index(prefix_sum: list[int], left: int, right: int) -> int:

    if left >= 1:
        return prefix_sum[right] - prefix_sum[left - 1]
    else:
        return prefix_sum[right]


def main():
    _, m = map(int, input().split())
    regiments = list(map(int, input().split()))

    prefix_sum = calc_prefix_sum(regiments)

    for i in range(m):
        numbers_of_regiments, target_sum = map(int, input().split())
        res = find_number_of_start_regiment_for_sortie(
            prefix_sum,
            numbers_of_regiments,
            target_sum,
        )
        print(res)


if __name__ == "__main__":
    main()
