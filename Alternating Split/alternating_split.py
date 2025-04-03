"""
A module for solution for alternating split task.
"""
class Node:
    """
    A class for initializing node.
    """
    def __init__(self, data=None):
        """
        Initializing variables.
        """
        self.data = data
        self.next = None

class Context:
    """
    A class for solution for alternating split task
    """
    def __init__(self, first, second):
        """
        Initializing variables.
        """
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Splits the linked list into two lists with alternating nodes.
    """
    if not head or not head.next:
        raise ValueError("List must contain at least two nodes")
    first_head = head
    second_head = head.next
    first_current = first_head
    second_current = second_head
    current = head.next.next
    is_first = True
    while current:
        if is_first:
            first_current.next = current
            first_current = first_current.next
        else:
            second_current.next = current
            second_current = second_current.next
        current = current.next
        is_first = not is_first
    first_current.next = None
    second_current.next = None
    return Context(first_head, second_head)
