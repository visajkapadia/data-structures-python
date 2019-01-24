class BNode:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data


class BinarySearchTree:

    root = None

    def insert(self, ptr, data):
        if ptr is None:
            new_node = BNode(data)
            self.root = new_node
            return
        if data < ptr.data:
            if ptr.left is None:
                new_node = BNode(data)
                ptr.left = new_node
            else:
                self.insert(ptr.left, data)
        else:
            if ptr.right is None:
                new_node = BNode(data)
                ptr.right = new_node
            else:
                self.insert(ptr.right, data)

    def get_root(self):
        return self.root

    def print_tree(self, root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.data)
        self.print_tree(root.right)