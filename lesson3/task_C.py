def find_min_numbers_amount_to_delete(nums: list[int]) -> int:

    hm = {}
    for num in nums:
        hm[num] = hm.get(num, 0) + 1

    hm = list(sorted(hm.items(), key=lambda x: x[0]))
    total = len(nums)
    ln = len(hm)
    minn = total - hm[0][1]
    for i in range(ln - 1):
        elem_left, cnt_left = hm[i]
        elem_right, cnt_right = hm[i + 1]
        minn = min(minn, total - cnt_left)
        if elem_right - elem_left <= 1:
            minn = min(minn, total - cnt_right - cnt_left)

    return minn


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    res = find_min_numbers_amount_to_delete(nums)
    print(res)
