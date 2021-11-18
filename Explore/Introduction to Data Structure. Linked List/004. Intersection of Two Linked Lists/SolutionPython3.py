# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cl = headA
        cr = headB
        cc = {}
        while cl != None:
            cc[cl] = 1
            cl = cl.next
        while cr != None:
            if cr in cc:
                return cr
            else:
                cr = cr.next
        return None