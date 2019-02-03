def reverse_stack(self):
    queue = []

    while not self.is_empty():
        queue.append(self.pop())

    while len(queue) != 0:
        self.push(queue.pop(0))