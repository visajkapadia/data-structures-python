class Stack:

    def __init__(self):
        self.s = []

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.s.pop()

    def push(self, data):
        self.s.append(data)

    def is_empty(self):
        return len(self.s) == 0

    def print_stack(self):
        print(self.s)
