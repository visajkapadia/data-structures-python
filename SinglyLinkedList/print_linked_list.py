def print_list(self):
    # 0(n)
    ptr = self.head

    while ptr is not None:
        if ptr.next is None:
            print("(", ptr.data, ")", end=" ")
        else:
            print("(", ptr.data, ")", end="->")
        ptr = ptr.next