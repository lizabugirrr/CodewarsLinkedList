"""
A module for solution to get nth node task.
"""
class Node:
    """
    A class to initializa node data.
    """
    def __init__(self, data, next=None):
        """
        Initializing variables.
        """
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    A solution function.
    """
    if node is None:
        raise Exception("Invalid index: list is empty")
    current = node
    count = 0
    while current:
        if count == index:
            return current
        current = current.next
        count += 1
    raise Exception("Invalid index: out of range")
