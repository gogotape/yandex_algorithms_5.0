def is_some_values_repeating(nums: list[int], k: int) -> str:
    l, r = 0, k - 1
    ln = len(nums)
    window = set(nums[l:r + 1])
    while r < ln - 1:
        r += 1
        elem = nums[r]
        if elem in window:
            return "YES"
        window.remove(nums[l])
        window.add(elem)
        l += 1
    return "NO"


if __name__ == '__main__':
    n, k  = map(int, input().split())
    nums = list(map(int, input().split()))
    res = is_some_values_repeating(nums, k)
    print(res)


if __name__ == '__main__':
    n, k  = map(int, input().split())
    nums = list(map(int, input().split()))
    res = is_some_values_repeating(nums, k)
    print(res)
