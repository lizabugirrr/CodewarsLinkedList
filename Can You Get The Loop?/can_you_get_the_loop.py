"""
A module for solution for can you get the loop task.
"""
def loop_size(node):
    """
    A solution for can you get the loop task.
    """
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0
    count = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        count += 1
    return count
