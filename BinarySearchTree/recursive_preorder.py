# from BinarySearchTree.binary_search_tree import BinarySearchTree


def recursive_preorder(ptr):
    if ptr:
        print(ptr.data, end=" ")
        recursive_preorder(ptr.left)
        recursive_preorder(ptr.right)


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# recursive_preorder(bst.get_root())
