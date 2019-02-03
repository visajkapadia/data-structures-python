# from BinarySearchTree.binary_search_tree import BinarySearchTree


def height(ptr):
    if ptr is None:
        return -1
    return 1 + max(height(ptr.left), height(ptr.right))


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# bst.insert(6)
# bst.insert(8)
# print(height(bst.get_root()))



