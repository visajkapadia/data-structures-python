# from BinarySearchTree.binary_search_tree import BinarySearchTree


def search(ptr, key):
    if ptr is None:
        return False
    if ptr.data == key:
        return True
    if ptr.data > key:
        return search(ptr.left, key)
    return search(ptr.right, key)


# bst = BinarySearchTree()
# bst.insert(3)
# bst.insert(1)
# bst.insert(5)
# print(search(bst.get_root(), 5))
# print(search(bst.get_root(), 17))
