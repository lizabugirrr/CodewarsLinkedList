"""
A module for solution to convert a linked list to a string.
"""
def stringify(node):
    """
    A solution function.
    """
    if node is None:
        return "None"
    result = ""
    current = node
    while current:
        result += str(current.data) + " -> "
        current = current.next
    result += "None"
    return result
