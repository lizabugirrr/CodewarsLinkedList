"""
A solution to push & buildonetwothree task.
"""
class Node:
    """
    A class for innitializing node data.
    """
    def __init__(self, data):
        """
        Initializing variables.
        """
        self.data = data
        self.next = None

def push(head, data):
    """
    A solution function to task.
    """
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """
    A solution function to task.
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
