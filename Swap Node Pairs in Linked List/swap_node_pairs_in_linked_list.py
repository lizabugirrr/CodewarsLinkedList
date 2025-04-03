"""
A module for solution to swap node pairs in linked list task.
"""
class Node:
    """
    A class for initializing node.
    """
    def __init__(self, next=None):
        """
        Initializing variables.
        """
        self.next = next

def swap_pairs(head):
    """
    A solution to task.
    """
    if not head or not head.next:
        return head
    dummy = Node()
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next
