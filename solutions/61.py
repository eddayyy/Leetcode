# Title: Rotate List
# Category: Linked List
# Difficulty: Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Problem:
Given a linked list rotate the list to the right by k places 

Thoughts: 
1. Convert linked list to a circular linked list 

Solution:
- The new tail of the linked list will be
  new_tail_idx = length - (k%length) 
  the head will be new_tail.next 
  return new_head  
'''

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None 

        length = 1
        curr = head
        while curr.next: 
            length += 1 
            curr = curr.next
        curr.next = head 

        k %= length 
        steps_to_new_tail = length - k 
        new_tail = head 
        for _ in range(steps_to_new_tail - 1): 
            new_tail = new_tail.next
        new_head = new_tail.next 
        new_tail.next = None 
        return new_head