class MyQueueLinked:
    def __init__(self) -> None:
        self.queue = []

    def get(self):
        if self.queue == []:
            return 'error'
        return self.queue.pop()

    def put(self, num: int):
        self.queue.insert(0, num)

    def size(self):
        return len(self.queue)


def get_input():
    command_count = int(input().strip())

    commands = []

    for i in range(command_count):
        command = input().strip()
        commands.append(command)

    return commands


def main():
    queue_linked = MyQueueLinked()

    commands = get_input()

    for command in commands:
        if 'put' in command:
            queue_linked.put(int(command.split()[1]))
        else:
            print(getattr(queue_linked, command)())


if __name__ == '__main__':
    main()
