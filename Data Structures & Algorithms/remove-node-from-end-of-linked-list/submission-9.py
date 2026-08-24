# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()

        tail = dummy

        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        remove = count - n

        cur = head
        for node in range(remove):
            tail.next = cur
            cur = cur.next
            tail = tail.next
        tail.next = cur.next
        return dummy.next