
'''
Problem:
Given a linked list determine if the linked list is a palindrome.

Questions:
Are there duplicate elements in the linked list? 

Thought process:
A naive approach would be to turn the linked list into a dynamic array and compare the array to the reverse of itself. This would use O(n) space and O(n) time. 

Solution: 

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True 
        res = [] 
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]