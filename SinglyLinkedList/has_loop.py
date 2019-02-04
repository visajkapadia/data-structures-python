def has_loop(self):
    # O(n)
    ptr = self.get_head()
    hash = {}

    if ptr is None:
        return False

    while ptr is not None:
        if ptr in hash:
            return True
        else:
            hash[ptr] = ''
            ptr = ptr.next

    return False





