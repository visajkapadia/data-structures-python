# from BinarySearchTree.binary_search_tree import BinarySearchTree


def unival_tree(ptr):
    if ptr is None:
        return 0

    if ptr.left is None and ptr.right is None:
        return 1

    if ptr.left is not None and ptr.right is None:
        if ptr.data == ptr.left.data:
            return 1 + unival_tree(ptr.left)
        else:
            return unival_tree(ptr.left)

    if ptr.right is not None and ptr.left is None:
        if ptr.data == ptr.right.data:
            return 1 + unival_tree(ptr.right)
        else:
            return unival_tree(ptr.right)

    if ptr.data == ptr.left.data == ptr.right.data:
        return 1 + unival_tree(ptr.left) + unival_tree(ptr.right)

    return unival_tree(ptr.left) + unival_tree(ptr.right)


# bst = BinarySearchTree()
# bst.insert(1)
# bst.insert(1)
# bst.insert(1)
# print(unival_tree(bst.get_root()))


