def main(lst):

    res = (lst[0] % 2) == 0   # True - четное
    answer = ""
    for i in range(len(lst) - 1):
        left, right = res, (lst[i + 1]) % 2 == 0
        if not left and not right:
            res = False
            answer += "x"
        elif left and right:
            res = True
            answer += "+"
        else:
            res = False
            answer += "+"

    return answer


if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    print(main(lst))

