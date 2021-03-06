'''
depth first values
Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
test_02:
a = Node('a')
#     a
depth_first_values(a) 
#   -> ['a']
test_03:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b;
b.left = c;
c.right = d;
d.right = e;

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

depth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e']
test_04:
depth_first_values(None) 
#   -> []
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    # Iterative
    # return depth_first_values_iterative(root)

    # Recursive
    # values = []
    # depth_first_values_recursive(root, values)
    # return values

    # Recursive 2
    return depth_first_values_recursive2(root)


def depth_first_values_iterative(root):
    if root is None:
        return []

    values = []
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        values.append(curr.val)

        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    return values


def depth_first_values_recursive(root, values):
    if root is None:
        return

    values.append(root.val)
    depth_first_values_recursive(root.left, values)
    depth_first_values_recursive(root.right, values)


def depth_first_values_recursive2(root):
    if root is None:
        return []

    return [root.val] + depth_first_values_recursive2(root.left) + depth_first_values_recursive2(root.right)


# test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
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

assert depth_first_values(a) == ['a', 'b', 'd', 'e', 'c', 'f']
# test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

assert depth_first_values(a) == ['a', 'b', 'd', 'e', 'g', 'c', 'f']
# test_02:
a = Node('a')
#     a
assert depth_first_values(a) == ['a']
# test_03:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b
b.left = c
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

assert depth_first_values(a) == ['a', 'b', 'c', 'd', 'e']
# test_04:
assert depth_first_values(None) == []

print("All tests passed")
