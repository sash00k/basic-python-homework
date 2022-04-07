LST = [("Alice", 160), ("John", 180), ("Karen", 163), ("Michael", 182), ("Peter", 172)]


def height_sort(lst):
    lst.sort(key=lambda x: x[1])


if __name__ == '__main__':
    height_sort(LST)
    print(LST)
