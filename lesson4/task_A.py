hm = {}


def binary_search(arr, target, most_left=True):

    ln = len(arr)

    l, r = 0, ln - 1
    mid = 0

    while l <= r:

        mid = (r - l) // 2 + l

        if mid - 1 >= 0 and mid + 1 < ln and (arr[mid - 1] < target < arr[mid]):
            if most_left:
                return mid
            else:
                return mid - 1

        if mid - 1 >= 0 and mid + 1 < ln and (arr[mid] < target < arr[mid + 1]):
            if most_left:
                return mid + 1
            else:
                return mid

        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1

        if arr[mid] == target:
            if most_left:
                while mid >= 0 and arr[mid] == target:
                    mid -= 1
                return mid + 1
            else:
                while mid < ln and arr[mid] == target:
                    mid += 1
                return mid - 1

    return mid


def how_much_numbers_between(array, left, right) -> int:
    if len(hm) > 10:
        to_del = next(iter(hm.keys()))
        hm.pop(to_del)
    res = hm.get((left, right))
    if res:
        return res

    if left < array[0] and right > array[-1]:
        res = len(array)

    elif right < array[0] or left > array[-1]:
        res = 0

    else:
        l = binary_search(array, left)
        r = binary_search(array, right, most_left=False)

        if r < l:
            res = 0
        else:
            res = r - l + 1

    hm[(left, right)] = res

    return res


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    arr = sorted(arr)

    results = []
    for i in range(k):
        left, right = map(int, input().split())
        res = how_much_numbers_between(arr, left, right, i)
        results.append(res)

    print(*results)
