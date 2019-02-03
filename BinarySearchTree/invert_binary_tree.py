# from BinarySearchTree.binary_search_tree import BinarySearchTree
# from BinarySearchTree.recursive_inorder_traverse import recursive_inorder


def invert_tree(ptr):
    if ptr is None or (ptr.left is None and ptr.right is None):
        return

    ptr.left, ptr.right = ptr.right, ptr.left

    invert_tree(ptr.left)
    invert_tree(ptr.right)


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# recursive_inorder(bst.get_root())
# print()
#
# invert_tree(bst.get_root())
# recursive_inorder(bst.get_root())
