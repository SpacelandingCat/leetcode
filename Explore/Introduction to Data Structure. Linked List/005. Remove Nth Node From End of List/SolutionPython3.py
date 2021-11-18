# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cp = head
        while cp != None:
            cp = cp.next
            l += 1
        if l == 1:
            head = None
            return head
        if l == n:
            head = head.next
            return head
        if n == 1:
            cp = head
            i = 1
            while i < l - 1:
                cp = cp.next
                i += 1
            cp.next = None
            return head
        l -= n
        cp = head
        cn = head.next
        cn = cn.next
        i = 1
        while i < l:
            cp = cp.next
            cn = cn.next
            i += 1
        cp.next = cn
        return head
