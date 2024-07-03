# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        elif head.next is None:
            return head
        
        odd, even = head, head.next
        evenHead = even
        while even != None and even.next != None:
            odd.next = even.next 
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        return head