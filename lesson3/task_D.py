def is_some_values_repeating(nums: list[int], k: int) -> str:
    l, r = 0, 0
    ln = len(nums)
    window = set()
    while r < ln:
        elem = nums[r]
        if elem in window:
            return "YES"
        window.add(elem)

        if r - l + 1 > k:
            window.remove(nums[l])
            l += 1
        r += 1

    return "NO"


if __name__ == '__main__':
    n, k  = map(int, input().split())
    nums = list(map(int, input().split()))
    res = is_some_values_repeating(nums, k)
    print(res)
