'''
linked list values
Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
test_01:
x = Node("x")
y = Node("y")

x.next = y

# x -> y

linked_list_values(x) # -> [ 'x', 'y' ]
test_02:
q = Node("q")

# q

linked_list_values(q) # -> [ 'q' ]
test_03:
linked_list_values(None) # -> [ ]
'''


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
    # accumulate values in 'values' list through the function
    linked_list_values_recursive2(node, values)
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
