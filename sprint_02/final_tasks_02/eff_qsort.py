# 85060650

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int
    penalties: int

    def __gt__(self, other):
        if self.score == other.score:
            if self.penalties == other.penalties:
                return self.name > other.name
            return self.penalties > other.penalties
        return self.score < other.score

    def __lt__(self, other):
        return other > self

    def __str__(self):
        return self.name


def qsort_in_place(array, left, right):
    if left >= right:
        return

    i, j = left, right

    pivot = array[(left + right) // 2]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    qsort_in_place(array, left, j)
    qsort_in_place(array, i, right)


def get_input():
    length = int(input().strip())
    contestants = []
    for i in range(length):
        name, score, penalties = input().strip().split()
        contestants.append(Student(name, int(score), int(penalties)))

    return length, contestants


def main():
    length, array = get_input()

    qsort_in_place(array, 0, length - 1)

    for elem in array:
        print(elem)


if __name__ == '__main__':
    main()
