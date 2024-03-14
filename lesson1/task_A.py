def task_A(p, v, q, m):
    left = p - v, p + v
    right = q - m, q + m

    res = 0

    if left[0] <= right[0]:
        pass
    else:
        left, right = right, left

    if left[0] <= right[0] and left[1] >= right[1]:
        res = left[1] - left[0] + 1
    elif left[1] < right[0]:
        res = left[1] - left[0] + right[1] - right[0] + 2
    elif left[1] >= right[0]:
        res = right[1] - left[0] + 1

    return res
