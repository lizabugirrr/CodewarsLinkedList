"""
A module for solution to sorted insert task.
"""
class Node:
    """
    A class for solutiobn to sorted insert task.
    """
    def __init__(self, data):
        """
        Initiallizing variables.
        """
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    A solution function.
    """
    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head
