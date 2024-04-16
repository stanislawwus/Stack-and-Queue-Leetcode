class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def push(self, data):
        temp = Node(data)

        if self.rear is None:
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp

    def pop(self):
        if self.is_empty():
            return None

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.push(x)

        while not self.q1.is_empty():
            self.q2.push(self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.is_empty():
            return None
        return self.q1.pop()

    def top(self):
        if self.q1.is_empty():
            return None
        return self.q1.front.data

    def empty(self):
        return self.q1.is_empty()
