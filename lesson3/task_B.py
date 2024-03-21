def is_anagram(a, b):

    hm = {}
    for char in a:
        hm[char] = hm.get(char, 0) + 1

    for char in b:
        hm[char] = hm.get(char, 0) - 1
        if hm[char] == 0:
            del hm[char]

    return "YES" if not hm else "NO"


if __name__ == "__main__":
    a, b = input(), input()
    res = is_anagram(a, b)
    print(res)
