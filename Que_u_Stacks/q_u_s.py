class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        prev = None
        data = self.head
        while self.head.next is not None:
            prev = data
            data = self.head.next
        prev.next = None

    def pop_last(self):
        if self.is_empty():
            return None
        pop_node = self.head
        self.head = self.head.next
        return pop_node.data

    def is_empty(self):
        return self.head is None

class MyQueue:
    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop_last())
        return self.stack2.pop_last()

    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop_last())
        return self.stack2.head.data

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()
