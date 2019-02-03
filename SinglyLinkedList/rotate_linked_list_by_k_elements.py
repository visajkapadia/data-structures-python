def rotate_linked_list_by_k(self, k):
    # 0(n)
    if k <= 0:
        return

    length = self.length()

    if k >= length:
        return

    if length == 0 or length == 1:
        return

    if length == 2:
        ptr = self.head.next
        ptr.next = self.head
        self.head.next = None
        self.head = ptr
        return

    ptr = self.head.next
    temp = self.head
    count = 0

    while count != (k - 1):
        self.head = self.head.next
        ptr = ptr.next
        count += 1

    self.head.next = None
    self.head = ptr

    while ptr.next is not None:
        ptr = ptr.next

    ptr.next = temp