def search(self, data):
    # 0(n)
    if self.head is None:
        return False

    ptr = self.head

    while ptr is not None:
        if ptr.data == data:
            return True
        ptr = ptr.next

    return False





