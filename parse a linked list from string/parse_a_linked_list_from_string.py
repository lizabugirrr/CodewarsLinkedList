"""
A module for solution to parse a linked list from a string.
"""

class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
      
def linked_list_from_string(string):
    """
    A solution function.
    """
    if string == "null":
        return None
    parts = string.split(" -> ")
    values = parts[:-1]
    if not values:
        return None
    head = Node(int(values[0]))
    current = head
    for value in values[1:]:
        current.next = Node(int(value))
        current = current.next
    return head
