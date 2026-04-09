# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of list
        cur = head
        lenList = 0
        while cur:
            cur = cur.next
            lenList += 1

        removeIndex = lenList - n
        if removeIndex == 0:
            return head.next
        
        cur = head
        for i in range(lenList - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head