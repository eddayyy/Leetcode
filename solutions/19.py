# Title: Remove Nth Node From End of List
# Category: Linked List
# Difficulty: Medium 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both first and second pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # second now points to the node before the one to be deleted
        second.next = second.next.next
        
        return dummy.next