# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        h = head
        c = head
        l = 1
        while c.next != None:
            c = c.next
            l += 1
        c.next = h
        s = l - (k % l)
        while s > 0:
            s -= 1
            c = c.next
            h = h.next
        c.next = None
        head = h
        return head
