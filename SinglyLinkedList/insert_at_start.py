def insert_at_start(self, data):
    # 0(1)
    new_node = self.create_newnode(data)

    if self.head is None:
        self.head = new_node
        return

    new_node.next = self.head
    self.head = new_node