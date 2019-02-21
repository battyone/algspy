class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class LinkedListDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def add_first(self, val: int) -> None:
        node = Node(val)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.size += 1

    def add_last(self, val: int) -> None:
        node = Node(val)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def remove_first(self) -> int:
        if self.is_empty():
            raise ValueError("Can't remove from empty deque")
        val = self.head.val
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def remove_last(self) -> int:
        if self.is_empty():
            raise ValueError("Can't remove from empty deque")
        val = self.tail.val
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
