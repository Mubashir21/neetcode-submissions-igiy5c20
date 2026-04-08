# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        dummy = ListNode()
        tail = dummy
    
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1

        while l1 and l2:
            if l1.val >= l2.val:
                tail.next = l2
                tail = l2
                l2 = l2.next
            else:
                tail.next = l1
                tail = l1
                l1 = l1.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next
            