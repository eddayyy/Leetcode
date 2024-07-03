"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        def flattenChildren(node): 
            tail = node 
            while node:
                next_node = node.next
                if node.child:
                    child_tail = flattenChildren(node.child)

                    node.next = node.child
                    node.child.prev = node 

                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail 

                    else:
                        tail = child_tail

                    node.child = None 
                    node = child_tail
                else:
                    tail = node
                    node = next_node 
            return tail 

        flattenChildren(head)
        return head