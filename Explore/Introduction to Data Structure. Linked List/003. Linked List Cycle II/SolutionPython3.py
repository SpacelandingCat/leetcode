# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cs = head
        cf = head
        if head == None:
            return None
        if cf.next == None:
            return None
        else:
            cf = cf.next
        while cf.next != None and cf != cs:
            cs = cs.next
            cf = cf.next
            if cf.next != None:
                cf = cf.next
            else:
                return None
        if cf == cs:
            cfc = 1
            csc = 0
            cf = cf.next
            while cf != cs:
                cf = cf.next
                cf = cf.next
                cfc += 2
                cs = cs.next
                csc += 1
            cfc -= csc
            cs = head
            while cs.next != None:
                i = 0
                cf = cs.next
                while i <= cfc:
                    if cf.next == head:
                        return head
                    if cf.next == cs.next:
                        return cf.next
                    cf = cf.next
                    i += 1
                cs = cs.next
        return None