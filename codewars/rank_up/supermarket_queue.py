def queue_time(array, checkout):
    checkouts = [0] * checkout

    checkouts[0] = array.pop(0)

    for elem in array:
        checkouts[checkouts.index(min(checkouts))] += elem

    return max(checkouts)


def main():
    print(queue_time([10,2,3,15], 2))


if __name__ == '__main__':
    main()
