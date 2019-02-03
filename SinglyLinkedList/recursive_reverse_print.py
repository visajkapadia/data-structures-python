def reverse_print_recursive(self, start):
    if start is None:
        return

    if start.next is None:
        print(start.data)
        return

    prev = start
    curr = prev.next

    if curr.next is None:
        print(curr.data)
        print(prev.data)
        return

    self.reverse_print_recursive(prev.next)

    print(prev.data)