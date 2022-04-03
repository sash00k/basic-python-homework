import random
import typing as t

INITIAL_CAPACITY = 10 ** 2
MULTIPLIER = 4
EXPANSION_ON = 0.5


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class HashTable:

    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.storage = [Node(None)] * self.capacity
        self.expand_times = 0

    def hash(self, value) -> int:
        return hash(value) % self.capacity

    def add(self, value) -> t.Optional[int]:
        self.size += 1
        index = self.hash(value)
        node = self.storage[index]

        if node.value is None:
            self.storage[index] = Node(value)
            return index

        parent = node
        while node is not None:
            parent = node
            node = node.next
        parent.next = Node(value)
        return index

    def find(self, value) -> t.Optional[int]:
        index = self.hash(value) % self.capacity
        node = self.storage[index]
        while node.value != value:
            node = node.next
            if node.value is None:
                return None
        return index

    def delete(self, value) -> bool:
        index = self.hash(value) % self.capacity
        node = self.storage[index]
        parent = None

        while node.value != value:
            node = node.next
            if node.value is None:
                return False

        self.size -= 1
        if parent is None:
            self.storage[index] = node.next
        else:
            parent.next = node.next
        return True

    def print_table(self):
        for index in range(self.capacity):
            print('['+str(index)+']:', end=' ')
            node = self.storage[index]
            while node is not None:
                if node.value is not None:
                    print(str(node.value), end=' ')
                node = node.next
            print()

    def check(self) -> bool:
        # вернет True, если надо расширяться, False - если нет
        return True if self.size / self.capacity > EXPANSION_ON else False

    def expand(self):
        self.storage += [Node(None)] * self.capacity
        self.capacity *= 2


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.print_table()
    for _ in range(INITIAL_CAPACITY // MULTIPLIER):
        hash_table.add(random.choice(range(INITIAL_CAPACITY * MULTIPLIER)))

    hash_table.print_table()

