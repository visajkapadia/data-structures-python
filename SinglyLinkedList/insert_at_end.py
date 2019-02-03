def insert_at_end(self, data):
    # 0(n)
    new_node = self.create_newnode(data)

    if self.head is None:
        self.head = new_node
        return

    ptr = self.head

    while ptr.next is not None:
        ptr = ptr.next

    ptr.next = new_node
