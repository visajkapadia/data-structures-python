class LNode:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class SinglyLinkedList:
    start = None

    def delete_node_with_given_key(self, data):
        pass

    def delete_nth_node(self, n):
        pass

    def delete_linked_list(self):
        self.start = None

    def sort(self):
        pass

    def length(self):
        # 0(n)
        if self.start is None:
            return 0

        length = 0
        ptr = self.start
        while ptr is not None:
            length += 1
            ptr = ptr.next

        return length

    def search(self, data):
        # 0(n)
        if self.start is None:
            return False

        ptr = self.start

        while ptr is not None:
            if ptr.data == data:
                return True
            ptr = ptr.next

        return False

    def insert_at_start(self, data):
        # 0(1)
        new_node = LNode(data)

        if self.start is None:
            self.start = new_node
            return

        new_node.next = self.start
        self.start = new_node

    def insert_at_end(self, data):
        # 0(n)
        new_node = LNode(data)

        if self.start is None:
            self.start = new_node
            return

        ptr = self.start

        while ptr.next is not None:
            ptr = ptr.next

        ptr.next = new_node

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
            self.start = curr
            curr.next = prev
            prev.next = None
            return

        self.reverse_recursive(prev.next)

        curr.next = prev
        prev.next = None

    def reverse_iterative(self):
        # 0(n)
        if self.start is None:
            # if 0 elements
            return

        if self.start.next is None:
            # if single element
            return

        if self.start.next.next is None:
            # if two elements
            ptr = self.start.next
            ptr.next = self.start
            self.start.next = None
            self.start = ptr
            return

        # we have to set atleast 3 base cases for setting up these three pointers
        prev = self.start
        curr = prev.next
        nxt = curr.next

        while nxt is not None:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next

        self.start.next = None
        self.start = curr
        curr.next = prev

    def get_start(self):
        return self.start

    def print_list(self):
        # 0(n)
        ptr = self.start

        while ptr is not None:
            if ptr.next is None:
                print("(", ptr.data, ")", end=" ")
            else:
                print("(", ptr.data, ")", end="->")
            ptr = ptr.next

    def reverse_print_recursive(self, start):
        if start is None:
            return

        if start.next is None:
            print(start.data)
            return

        prev = start
        curr = prev.next

        if curr.next is None:
            print(curr.data)
            print(prev.data)
            return

        self.reverse_print_recursive(prev.next)

        print(prev.data)

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
            ptr = self.start.next
            ptr.next = self.start
            self.start.next = None
            self.start = ptr
            return

        ptr = self.start.next
        temp = self.start
        count = 0

        while count != (k-1):
            self.start = self.start.next
            ptr = ptr.next
            count += 1

        self.start.next = None
        self.start = ptr

        while ptr.next is not None:
            ptr = ptr.next

        ptr.next = temp

