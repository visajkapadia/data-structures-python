# from BinarySearchTree.binary_search_tree import BinarySearchTree


def recursive_inorder(ptr):
    if ptr:
        recursive_inorder(ptr.left)
        print(ptr.data, end=" ")
        recursive_inorder(ptr.right)


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# recursive_inorder(bst.get_root())
