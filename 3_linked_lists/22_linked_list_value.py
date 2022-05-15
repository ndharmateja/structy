'''
get node value
Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 2) # 'c'
test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 3) # 'd'
test_02:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 7) # None
test_03:
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

get_node_value(node1, 0) # 'banana'
test_04:
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

get_node_value(node1, 1) # 'mango'
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_node_value(head, index):
    # Iterative
    # return get_node_value_iterative(head, index)

    # Recursive
    return get_node_value_recursive(head, index, 0)


def get_node_value_iterative(head, index):
    if head is None:
        return None
    curr = head
    curr_index = 0
    while curr is not None:
        if curr_index == index:
            break
        curr = curr.next
        curr_index += 1

    return None if curr is None else curr.val


def get_node_value_recursive(head, index, curr_index):
    if head is None:
        return None
    if index == curr_index:
        return head.val
    return get_node_value_recursive(head.next, index, curr_index + 1)


# test_00
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

assert get_node_value(a, 2) == 'c'

# test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

assert get_node_value(a, 3) == 'd'

# test_02:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

assert get_node_value(a, 7) == None

# test_03:
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

assert get_node_value(node1, 0) == 'banana'

# test_04:
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

assert get_node_value(node1, 1) == 'mango'
print("All tests passed")
