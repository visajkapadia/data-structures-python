def length(self):
    # 0(n)
    if self.head is None:
        return 0

    length = 0
    ptr = self.head
    while ptr is not None:
        length += 1
        ptr = ptr.next

    return length