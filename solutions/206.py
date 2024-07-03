class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head: return None
      if not head.next: return head

      prev, curr = None, head
      while curr:
        curr.next, prev, curr = prev, curr, curr.next
      return prev