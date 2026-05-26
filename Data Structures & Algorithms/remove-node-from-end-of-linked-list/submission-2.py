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
        
        n  = count - n
        dummy = ListNode()
        tail = dummy
        cur = head
        count = 0

        while count < n:
            tail.next = cur
            tail = tail.next
            cur = cur.next
            count += 1
        tail.next = cur.next
        return dummy.next
            