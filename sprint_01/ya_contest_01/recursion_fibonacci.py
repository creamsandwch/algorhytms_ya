def get_commits_count(workers_count: int, stack=[1, 1]):
    if workers_count == 1 or workers_count == 0:
        return stack.pop()
    value = stack.pop()
    value_prev = stack.pop()
    stack.append(value)
    stack.append(value + value_prev)
    workers_count = workers_count - 1
    return get_commits_count(workers_count=workers_count, stack=stack)


def main():
    workers_count = int(input().strip())
    print(get_commits_count(workers_count=workers_count))


if __name__ == '__main__':
    main()
