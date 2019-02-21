class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("Can't pop from empty stack")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError("Can't peek from empty stack")
        return self.head.val

