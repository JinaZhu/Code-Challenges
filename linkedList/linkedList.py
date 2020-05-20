def deleteNode(node):
    # node's value is assign to node.next.val and node.next is now the next of next item
    node.val, node.next = node.next.val, node.next.next
