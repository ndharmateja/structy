class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(node):
    # Iterative
    return linked_list_values_iterative(node)


def linked_list_values_iterative(node):
    values = []
    curr = node
    while curr is not None:
        values.append(curr.val)
        curr = curr.next

    return values
