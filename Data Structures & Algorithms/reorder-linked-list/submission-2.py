# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = None
        cur = slow.next
        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = tail
            tail = cur
            cur = tmp
        
        cur = head
        while tail:
            tmptail = tail.next
            tmpcur = cur.next

            cur.next = tail
            tail.next = tmpcur

            cur = tmpcur
            tail = tmptail