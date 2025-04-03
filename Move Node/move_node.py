"""
A module for solution to move node task.
"""
class Node:
    """
    A class for node initializing.
    """
    def __init__(self, data):
        """
        Initializing variables.
        """
        self.data = data
        self.next = None

class Context:
    """
    A class for getting context data.
    """
    def __init__(self, source, dest):
        """
        Initializing variables.
        """
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    A solution function.
    """
    if source is None:
        raise Exception("Source list is empty")
    new_source = source.next
    source.next = dest
    new_dest = source
    return Context(new_source, new_dest)
