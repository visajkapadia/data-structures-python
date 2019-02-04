def get_nth_node(self, n):
    # O(n)
    if n < 0:
        return

    ptr = self.get_head()
    count = 0

    while count != n and ptr is not None:
        ptr = ptr.next
        count += 1

    if count == n:
        return ptr.data
