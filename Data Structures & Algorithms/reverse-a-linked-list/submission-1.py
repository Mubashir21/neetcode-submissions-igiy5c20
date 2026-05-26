# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = tail
            tail = cur
            cur = tmp
        
        return tail