# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Problem: 
Check if a Linked List has a cycle. 

Solution: 
Use Floyd's Tortoise and Hare algorithm, have a slow pointer and a fast pointer, if the 
fast pointer ever catches up to the slow pointer (they equal each other) then there is a cycle. 

'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False