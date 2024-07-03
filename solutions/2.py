class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution: 
        # Time  O(n) -> we're traversng a linked list which is an O(n) operation
        # Space O(n) -> We're creating a new linked list of length n 
        
        # Optimized Solution: 
        dummy = ListNode(0)
        current = dummy
        carry = 0 

        while l1 or l2: 
            l1_value = l1.val if l1 else 0 
            l2_value = l2.val if l2 else 0 
            
            total = l1_value + l2_value + carry
            carry = total // 10
            current_sum = total % 10

            current.next = ListNode(current_sum) 
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            current.next = ListNode(carry)
        
        return dummy.next