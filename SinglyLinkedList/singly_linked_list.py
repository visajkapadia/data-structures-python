class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def create_newnode(self, data):
        return LNode(data)

    from SinglyLinkedList.insert_at_end import insert_at_end
    from SinglyLinkedList.insert_at_start import insert_at_start
    from SinglyLinkedList.length import length
    from SinglyLinkedList.rotate_linked_list_by_k_elements import rotate_linked_list_by_k
    from SinglyLinkedList.reverse_recursive import reverse_recursive
    from SinglyLinkedList.reverse_iterative import reverse_iterative
    from SinglyLinkedList.recursive_reverse_print import reverse_print_recursive
    from SinglyLinkedList.print_linked_list import print_list
    from SinglyLinkedList.get_nth_node import get_nth_node
