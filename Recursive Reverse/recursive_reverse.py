"""
A module for solution to recursive reverse task.
"""
class Node:
    """
    A class for solution to recursive reverse task.
    """
    def __init__(self, data=None):
        """
        Initializing variables.
        """
        self.data = data
        self.next = None

def reverse(head):
    """
    A solution function.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head
