# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cs = head
        cf = head
        if head == None:
            return False
        if cf.next == None:
            return False
        else:
            cf = cf.next
        while cf.next != None and cf != cs:
            cs = cs.next
            cf = cf.next
            if cf.next != None:
                cf = cf.next
            else:
                return False
        if cf == cs:
            return True
        return False