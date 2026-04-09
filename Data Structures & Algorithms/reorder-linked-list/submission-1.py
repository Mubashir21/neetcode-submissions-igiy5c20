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
        tmp = slow.next
        slow.next = None
        slow = tmp
        while slow:
                tmp = slow.next
                slow.next = tail
                tail = slow
                slow = tmp                                                                                                                                                    
        
        # reorder list
        start, tail = head, tail
        while tail:
                tmpT = tail.next
                tmpS = start.next
                start.next = tail
                tail.next = tmpS
                start = tmpS
                tail = tmpT