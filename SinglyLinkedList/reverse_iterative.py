def reverse_iterative(self):
    # 0(n)
    if self.head is None:
        # if 0 elements
        return

    if self.head.next is None:
        # if single element
        return

    if self.head.next.next is None:
        # if two elements
        ptr = self.head.next
        ptr.next = self.head
        self.head.next = None
        self.head = ptr
        return

    # we have to set atleast 3 base cases for setting up these three pointers
    prev = self.head
    curr = prev.next
    nxt = curr.next

    while nxt is not None:
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next

    self.head.next = None
    self.head = curr
    curr.next = prev
