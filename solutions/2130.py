# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None: 
            return None 
        maximumSum = 0
        
        # Obtain the middle node of the linked list 
        slow, fast = head, head
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next

        current, prev = slow, None 

        # Reverse the second half of the linked list: 
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        


        start = head 
        while prev: 
            maximumSum = max(maximumSum, start.val + prev.val)
            prev = prev.next 
            start = start.next 
        
        return maximumSum 