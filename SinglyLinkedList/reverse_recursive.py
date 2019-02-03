def reverse_recursive(self, start):
    if start is None:
        return

    prev = start
    curr = prev.next

    if curr is None:
        # single element
        return

    if curr.next is None:
        # two elements
        self.head = curr
        curr.next = prev
        prev.next = None
        return

    self.reverse_recursive(prev.next)

    curr.next = prev
    prev.next = None