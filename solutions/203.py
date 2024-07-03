# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Create a next pointer = curr.next 
# Iterate through list and if curr.next.val = val 
# curr.next = curr.next.next 
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a sentinel node as a pseudohead, this will help handle the edge case 
        # where the head == val 
        # In that case we would be able to step over that 
        sentinel = ListNode(0)
        sentinel.next = head

        # Initialize our previous and current pointers
        # initially prev is the sentinel node, this val will never appear
        # when we return since we're always return sentinel.next 
        prev, curr = sentinel, head
       
        # iterate through the list while our current node is not null
        while curr:
            # If we encounter a node with val == val
            # we essentially break that off of the list making prev.next point to the element after curr
            # Not moving prev ahead is important here because we maintain a reference to a valid Node, if the 
            # rest of the nodes are invalid then prev will point to None per curr.next 
            if curr.val == val:
                prev.next = curr.next
            # If we haven't found a node we need to delete move prev forward
            else:
                prev = curr 
            # Move curr forward no matter what 
            curr = curr.next
        # Return the original head (if it's still there) 
        # if the whole list was == val then sentinel.next would = None 
        return sentinel.next 