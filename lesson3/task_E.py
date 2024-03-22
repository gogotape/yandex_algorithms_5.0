def find_at_least_in_two_list_numbers(
        nums1: list[int],
        nums2: list[int],
        nums3: list[int],
) -> list[int]:

    nums1 = set(nums1)
    nums2 = set(nums2)
    nums3 = set(nums3)

    nums12 = nums1.intersection(nums2)
    nums23 = nums2.intersection(nums3)
    nums13 = nums1.intersection(nums3)

    nums = nums12.union(nums13).union(nums23)
    nums = list(nums)
    nums.sort()
    return nums


if __name__ == '__main__':
    nums_lists = []
    for _ in range(3):
        _ = input()
        nums = list(map(int, input().split()))
        nums_lists.append(nums)
    res = find_at_least_in_two_list_numbers(*nums_lists)
    print(*res)
