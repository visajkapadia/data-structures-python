def sort_stack_using_temporary_stack(self):
    temp_stack = self.create_stack()
    another_stack = self.create_stack()

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