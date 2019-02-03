# from BinarySearchTree.binary_search_tree import BinarySearchTree
# from Stack.stack import Stack


def inorder(root):
    if root is None:
        return

    s = Stack()
    ptr = root

    while True:
        if ptr is not None:
            s.push(ptr)
            ptr = ptr.left
        else:
            if s.is_empty():
                break
            x = s.pop()
            print(x.data, end=" ")
            ptr = x.right


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# inorder(bst.get_root())
