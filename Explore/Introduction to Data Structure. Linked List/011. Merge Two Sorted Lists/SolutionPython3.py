# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return l1
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l = ListNode(l1.val)
            l1 = l1.next
        else:
            l = ListNode(l2.val)
            l2 = l2.next
        p = l
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                n = ListNode(l1.val)
                l1 = l1.next
            else:
                n = ListNode(l2.val)
                l2 = l2.next
            p.next = n
            p = n
        if l2 == None:
            while l1 != None:
                n = ListNode(l1.val)
                l1 = l1.next
                p.next = n
                p = n
        else:
            while l2 != None:
                n = ListNode(l2.val)
                l2 = l2.next
                p.next = n
                p = n
        return l
