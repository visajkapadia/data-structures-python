class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

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

    def get_root(self):
        return self.root
