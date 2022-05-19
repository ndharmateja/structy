'''
tree sum
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

tree_sum(a) # -> 21
test_01:
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

tree_sum(a) # -> 10
test_02:
tree_sum(None) # -> 0
'''
from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    # Iterative
    return tree_sum_iterative(root)

    # Recursive
    # return tree_sum_recursive(root)


def tree_sum_iterative(root):
    if root is None:
        return 0

    total = 0
    q = Queue()
    q.put(root)
    while not q.empty():
        curr = q.get()
        total += curr.val

        if curr.left is not None:
            q.put(curr.left)
        if curr.right is not None:
            q.put(curr.right)

    return total


def tree_sum_recursive(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


# test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

assert tree_sum(a) == 21
# test_01:
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

assert tree_sum(a) == 10
# test_02:
assert tree_sum(None) == 0

print("All tests passed")
