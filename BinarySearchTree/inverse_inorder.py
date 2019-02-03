# from BinarySearchTree.binary_search_tree import BinarySearchTree


def inverse_inorder(ptr):
    if ptr:
        inverse_inorder(ptr.right)
        print(ptr.data, end=" ")
        inverse_inorder(ptr.left)


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# inverse_inorder(bst.get_root())

