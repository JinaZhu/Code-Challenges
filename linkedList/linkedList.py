def deleteNode(node):
    # node's value is assign to node.next.val and node.next is now the next of next item
    node.val, node.next = node.next.val, node.next.next

# Write a program to find the node at which the intersection of two singly linked lists begins.


def get_intersection_node(HeadA, headB):
    l1 = HeadA
    l2 = headB

    if l1 is None or l2 is None:
        return None

    while True:
        if l1 == l2:
            return l1

        if l1.next is None and l2.next is None:
            return None
        elif l1.next is None and l2.next is not None:
            l1 = headB
            l2 = l2.next
        elif l1.next is not None and l2 is None:
            l1 = l1.next
            l2 = HeadA
        else:
            l1 = l1.next
            l2 = l2.next
