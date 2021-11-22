# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ln = ListNode()
        s = ''
        sum = 0
        ln = l1
        while ln.next != None:
            s = str(ln.val)+s
            ln = ln.next
        s = str(ln.val)+s
        sum = int(s)
        s = ''
        ln = l2
        while ln.next != None:
            s = str(ln.val)+s
            ln = ln.next
        s = str(ln.val)+s
        sum += int(s)
        s = str(sum)
        lb = ListNode()
        ln = lb
        ln.val = int(s[len(s)-1])
        i = len(s)-1
        while i > 0:
            lb.next = ListNode(s[i-1])
            lb = lb.next
            i -= 1
        return ln
