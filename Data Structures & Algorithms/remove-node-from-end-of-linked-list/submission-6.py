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

        if n == 0:
            return head.next
        cur = head

        for i in range(count - 1):
            if (i + 1) == n:
                print(i)
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
            