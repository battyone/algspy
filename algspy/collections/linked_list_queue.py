class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def enqueue(self, val: int) -> None:
        node = Node(val)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise ValueError("Can't pop from empty queue")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError("Can't peek from empty queue")
        return self.head.val

