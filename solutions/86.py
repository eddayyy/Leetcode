# Title: Partition List
# Category: Linked List
# Difficulty: Medium 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None 
        less_head = ListNode(0) 
        greater_head = ListNode(0) 

        curr = head
        less_ptr = less_head
        greater_ptr = greater_head 
        while curr: 
            if curr.val < x: 
                less_ptr.next  = curr
                less_ptr =  less_ptr.next
            else: 
                greater_ptr.next = curr 
                greater_ptr = greater_ptr.next
            curr = curr.next 
        
        less_ptr.next = greater_head.next 
        greater_ptr.next = None
        return less_head.next