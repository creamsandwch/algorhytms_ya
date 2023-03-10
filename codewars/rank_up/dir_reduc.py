def dirReduc(array: list) -> list:
    if array == [] or len(array) == 1:
        return array

    opposite_dirs = {
        'EAST': 'WEST',
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'WEST': 'EAST',
    }

    i = 0

    while True:
        print(f'i={i}, array={array}')
        if (
            opposite_dirs[array[i]] == array[i + 1]
        ):
            print(f'array[{i + 1}] = {array[i + 1]}', end=' ')
            print(f'array[{i}] = {array[i]}.')
            array.remove(array[i + 1])
            array.remove(array[i])
            i = 0
        else:
            i += 1
        if i == (len(array) - 1) or array == []:
            break

    return array


def main():
    u = ["SOUTH", "NORTH", "SOUTH", "WEST"]
    print(dirReduc(array=u))


if __name__ == '__main__':
    main()
