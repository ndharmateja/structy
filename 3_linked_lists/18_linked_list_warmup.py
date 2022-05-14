class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")


# A -> B -> C -> D
a.next = b
b.next = c
c.next = d


def print_list(node):
    curr = node
    while curr is not None:
        print(curr.value)
        curr = curr.next


print_list(a)
