def comp(array1: list, array2: list) -> bool:
    if type(array1) != list or type(array2) != list:
        return False

    while array1 != []:
        elem = array1[0]
        if elem * elem not in array2:
            return False

        array1.remove(elem)
        array2.remove(elem * elem)

    if len(array1) != len(array2):
        return False
    return True


def main():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2))


if __name__ == '__main__':
    main()
