class Node:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data


class BinaryTree:
    root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            ptr = self.root

            while True:
                if data < ptr.data:
                    if ptr.left is None:
                        ptr.left = new_node
                        break
                    else:
                        ptr = ptr.left
                else:
                    if ptr.right is None:
                        ptr.right = new_node
                        break
                    else:
                        ptr = ptr.right

    def in_order(self, ptr):
        if ptr:
            self.in_order(ptr.left)
            print(ptr.data)
            self.in_order(ptr.right)

    def post_order(self, ptr):
        if ptr:
            self.in_order(ptr.left)
            self.in_order(ptr.right)
            print(ptr.data)

    def pre_order(self, ptr):
        if ptr:
            print(ptr.data)
            self.in_order(ptr.left)
            self.in_order(ptr.right)

    def inverse_inorder(self, ptr):
        if ptr:
            self.in_order(ptr.right)
            print(ptr.data)
            self.in_order(ptr.left)

    def invert_tree(self, ptr):
        if ptr is None or (ptr.left is None and ptr.right is None):
            return

        ptr.left, ptr.right = ptr.right, ptr.left

        self.invert_tree(ptr.left)
        self.invert_tree(ptr.right)

    def unival_tree(self, ptr):
        if ptr is None:
            return 0

        if ptr.left is None and ptr.right is None:
            return 1

        if ptr.left is not None and ptr.right is None:
            if ptr.data == ptr.left.data:
                return 1 + self.unival_tree(ptr.left)
            else:
                return self.unival_tree(ptr.left)

        if ptr.right is not None and ptr.left is None:
            if ptr.data == ptr.right.data:
                return 1 + self.unival_tree(ptr.right)
            else:
                return self.unival_tree(ptr.right)

        if ptr.data == ptr.left.data == ptr.right.data:
            return 1 + self.unival_tree(ptr.left) + self.unival_tree(ptr.right)

        return self.unival_tree(ptr.left) + self.unival_tree(ptr.right)

    def get_root(self):
        return self.root

    def inorder(self):
        if self.root is None:
            return

        s = Stack()
        ptr = self.root

        while True:
            if ptr is not None:
                s.push(ptr)
                ptr = ptr.left
            else:
                if s.is_empty():
                    break
                x = s.pop()
                print(x.data)
                ptr = x.right

    def height(self, ptr):
        if ptr is None:
            return -1
        return 1 + max(self.height(ptr.left), self.height(ptr.right))

    def search(self, ptr, key):
        if ptr is None:
            return False
        if ptr.data == key:
            return True
        if ptr.data > key:
            return self.search(ptr.left, key)
        return self.search(ptr.right, key)

    def path(self, ptr, key):
        global_path_list = []
        s = Stack()
        temp_list = []

        while True:
            if ptr is not None:
                s.push(ptr)
                temp_list.append(ptr.data)
                ptr = ptr.left
            else:
                if s.is_empty():
                    break
                global_path_list.append(temp_list)
                ptr = s.pop()
                ptr = ptr.right
                if ptr is None:
                    temp_list.pop()

        print(global_path_list)
