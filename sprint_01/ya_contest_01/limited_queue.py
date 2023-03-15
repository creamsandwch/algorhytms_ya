class MyQueueSized:
    def __init__(self, max_size: int) -> None:
        self.max_size = int(max_size)
        self.queue = [None] * self.max_size

        self.length = 0
        self.tail = 0
        self.head = 0

    def is_empty(self):
        return self.length == 0

    def push(self, value):
        if self.length != self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.length += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.length -= 1
        return popped_value

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.length


def get_input():
    commands_count = int(input().strip())
    max_size = int(input().strip())

    commands = []

    for i in range(commands_count):
        command = input().strip()
        if 'push' in command:
            command = command.split()
        commands.append(command)

    return max_size, commands


def main():
    max_size, commands = get_input()

    queue = MyQueueSized(max_size=max_size)

    for command in commands:
        if 'push' in command:
            queue.push(int(command[1]))
        else:
            print(getattr(queue, command)())


if __name__ == '__main__':
    main()
