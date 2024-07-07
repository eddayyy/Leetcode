# Title: Remove Duplicates from Sorted list II 
# Category: Linked List 
# Difficulty: Medium 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            # Move the right pointer to skip all duplicates
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            
            # Check if prev.next is still curr, which means no duplicates were found
            if prev.next == curr:
                prev = prev.next
            else:
                # Skip all duplicates
                prev.next = curr.next
            
            curr = curr.next
        
        return dummy.next