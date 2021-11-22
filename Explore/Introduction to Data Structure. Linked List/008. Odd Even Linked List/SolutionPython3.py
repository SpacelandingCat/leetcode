# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        l = 0
        while a != None:
            l += 1
            a = a.next
        if l < 3:
            return head
        if l == 3:
            a = head
            b = a.next
            c = b.next
            a.next = c
            c.next = b
            b.next = None
            return head
        a = head
        b = a.next
        c = b
        d = c.next
        e = d.next
        i = 0
        while True:
            if i > 0:
                a = a.next
                b = a.next
                c = e
                d = c.next
                e = d.next
            i += 1
            c.next = e
            d.next = b
            a.next = d
            if e == None:
                break
            if e.next == None:
                break
        return head
