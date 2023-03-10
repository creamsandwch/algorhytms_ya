def wave(people: str):
    result = []
    i = 0
    while i < len(people):
        if people[i] != ' ':
            result.append(people[:i] + people[i].capitalize() + people[i + 1:])

        i += 1
    return result


def main():
    people = 'two words'
    print(wave(people))


if __name__ == '__main__':
    main()
