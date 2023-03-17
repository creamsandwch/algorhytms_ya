def generate_hashtag(s: str):
    hashtag = ['#']
    if len(s) == 0 or len(s) >= 140:
        return False

    for elem in s.split():
        hashtag.append(elem.capitalize())
    return ''.join(hashtag)


def main():
    s = input().strip()
    return generate_hashtag(s=s)


if __name__ == '__main__':
    print(main())
