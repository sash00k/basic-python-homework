import random

MAX_NUM = 10**5


def qsort(left: int, right: int, lst: list):
    if left >= right: return

    i, j = left, right
    pivot = lst[random.randint(left, right)]

    while i <= j:
        while lst[i] < pivot: i += 1
        while lst[j] > pivot: j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i, j = i + 1, j - 1
    qsort(left=left, right=j, lst=lst)
    qsort(left=i, right=right, lst=lst)


def sort(tpl: tuple, reverse: bool = False) -> list:
    lst = list(tpl)
    qsort(left=0, right=len(lst)-1, lst=lst)
    return lst if not reverse else lst[::-1]


if __name__ == '__main__':
    numbers = tuple(random.randint(0, MAX_NUM) for _ in range(random.randint(0, MAX_NUM)))
    print(sort(numbers, reverse=False))
