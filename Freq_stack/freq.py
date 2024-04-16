from collections import deque

class FreqStack:
    def __init__(self):
        self.stack = deque()
        self.all_freq = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.all_freq.appendleft(self.stack.count(val)) 

    def pop(self) -> int:
        if not self.stack:
            return None
        freq = max(self.all_freq)
        val = self.stack[-(self.all_freq.index(freq)+1)]
        del self.stack[-(self.all_freq.index(freq)+1)]
        del self.all_freq[self.all_freq.index(freq)]
        return val
