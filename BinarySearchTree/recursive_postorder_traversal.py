# from BinarySearchTree.binary_search_tree import BinarySearchTree


def recursive_postorder(ptr):
    if ptr:
        recursive_postorder(ptr.left)
        recursive_postorder(ptr.right)
        print(ptr.data, end=" ")


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# recursive_postorder(bst.get_root())
