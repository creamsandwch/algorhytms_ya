def pig_it(text: str):
    words = text.split()
    res = []
    for word in words:
        if word[0].isalpha():
            res.append(word[1:] + word[0] + 'ay')
        else:
            res.append(word)

    return ' '.join(res)


if __name__ == '__main__':
    print(pig_it(input().strip()))
