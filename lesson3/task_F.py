def replace_words(dictionary: list[str], text: list[str]) -> list[str]:
    res = []
    dictionary = set(dictionary)
    for word_to_replace in text:
        for i in range(1, len(word_to_replace)):
            if word_to_replace[:i] in dictionary:
                res.append(word_to_replace[:i])
                break
        else:
            res.append(word_to_replace)
    return res


if __name__ == '__main__':
    dictionary = input().split()
    text = input().split()
    res = replace_words(dictionary, text)
    print(*res)
