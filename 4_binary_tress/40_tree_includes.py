'''
tree includes
Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_includes(a, "e")  # -> True
test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
tree_includes(a, "a")  # -> True
test_02:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_includes(a, "n")  # -> False
test_03:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

tree_includes(a, "f")  # -> True
test_04:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

tree_includes(a, "p")  # -> False
test_05:
tree_includes(None, "b")  # -> False
'''
from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, target):
    # Iterative
    return tree_includes_iterative(root, target)

    # Recursive
    # return tree_includes_recursive(root, target)


def tree_includes_recursive(root, target):
    if root is None:
        return False

    return root.val == target or tree_includes_recursive(
        root.left, target) or tree_includes_recursive(
        root.right, target)


def tree_includes_iterative(root, target):
    if root is None:
        return []

    queue = Queue()
    queue.put(root)
    while not queue.empty():
        curr = queue.get()
        if curr.val == target:
            return True
        if curr.left is not None:
            queue.put(curr.left)
        if curr.right is not None:
            queue.put(curr.right)

    return False
