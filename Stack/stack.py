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

    def reverse_stack(self):
        queue = []

        while not self.is_empty():
            queue.append(self.pop())

        while len(queue) != 0:
            self.push(queue.pop(0))

    def sort_stack_using_temporary_stack(self):
        temp_stack = Stack()
        another_stack = Stack()

        while not self.is_empty():
            element = self.pop()

            if temp_stack.is_empty():
                temp_stack.push(element)
            else:
                while (temp_stack.peep() is not None) and temp_stack.peep() < element:
                    another_stack.push(temp_stack.pop())

                temp_stack.push(element)

                while not another_stack.is_empty():
                    temp_stack.push(another_stack.pop())

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())


