"""
A module for solution to remove duplicates task.
"""
class Node:
    """
    A class for solution to remove duplicates task.
    """
    def __init__(self, data):
        """
        Initializing variables.
        """
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    A solution function.
    """
    if head is None:
        return None
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
