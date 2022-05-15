'''
linked list find
Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "c") # True
test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "d") # True
test_02:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "q") # False
test_03:
node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli

linked_list_find(node1, "jason") # True
test_04:
node1 = Node(42)

# 42

linked_list_find(node1, 42) # True
test_05:
node1 = Node(42)

# 42

linked_list_find(node1, 100) # False
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_find(head, target):
    # Iterative
    # return linked_list_find_iterative(head, target)

    # Recursive
    return linked_list_find_recursive(head, target)


# TC - O(n), SC - O(1)
def linked_list_find_iterative(head, target):
    if head is None:
        return False
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    return False


# TC - O(n), SC - O(n)
def linked_list_find_recursive(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find_recursive(head.next, target)


def test_00():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    assert linked_list_find(a, "c") == True
    assert linked_list_find(a, "q") == False


def test_01():
    node1 = Node("jason")
    node2 = Node("leneli")

    node1.next = node2

    # jason -> leneli
    linked_list_find(node1, "jason") == True


def test_02():
    node1 = Node(42)

    # 42
    assert linked_list_find(node1, 42) == True
    assert linked_list_find(node1, 100) == False


def run_tests():
    test_00()
    test_01()
    test_02()
    print("All tests passed")


run_tests()
