class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(node):
    # Iterative
    # return linked_list_values_iterative(node)

    # Recursive
    # return linked_list_values_recursive(node, [])

    # Recursive 2
    values = []
    linked_list_values_recursive2(node, values)  # accumulate values in 'values' list
    return values


def linked_list_values_iterative(node):
    values = []
    curr = node
    while curr is not None:
        values.append(curr.val)
        curr = curr.next

    return values


def linked_list_values_recursive(node, values):
    if node is None:
        return values

    values.append(node.val)
    return linked_list_values_recursive(node.next, values)


def linked_list_values_recursive2(node, values):
    if node is None:
        return

    values.append(node.val)
    linked_list_values_recursive2(node.next, values)
