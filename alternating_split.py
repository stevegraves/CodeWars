class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


# Best practice
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError('Bad input')

    orig_a, orig_b = a, b = Node(), Node()

    while head:
        a.next = Node(head.data)
        a = a.next
        a, b = b, a
        head = head.next

    return Context(orig_a.next, orig_b.next)
