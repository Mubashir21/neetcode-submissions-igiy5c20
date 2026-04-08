# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        tail = None
        while slow:
            tmp = slow.next
            slow.next = tail
            tail = slow
            slow = tmp
        
        # reorder list
        start, tail = head, tail
        while tail.next:
            tmpT = tail.next
            tmpS = start.next
            start.next = tail
            tail.next = tmpS
            start = tmpS
            tail = tmpT
