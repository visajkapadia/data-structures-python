class Stack:

    def __init__(self):
        self.s = []

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.s.pop()

    def peep(self):
        if self.is_empty():
            return
        else:
            return self.s[-1]

    def push(self, data):
        self.s.append(data)

    def is_empty(self):
        return len(self.s) == 0

    def print_stack(self):
        print(self.s)

    def create_stack(self):
        return Stack()

    from Stack.sort_stack_using_temporary_stack import sort_stack_using_temporary_stack
    from Stack.reverse_stack import reverse_stack




