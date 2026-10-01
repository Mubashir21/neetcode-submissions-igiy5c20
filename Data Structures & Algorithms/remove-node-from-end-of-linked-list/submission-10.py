# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head

        while cur:
            cur = cur.next
            count += 1
        
        dummy = ListNode()
        dummy.next = head
        diff = count -  n
        cur = dummy
        while diff > 0:
            cur = cur.next
            diff -= 1
        cur.next = cur.next.next
        return dummy.next