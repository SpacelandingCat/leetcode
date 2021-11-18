# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        c = head
        cn = head.next
        head.next = None
        while cn.next != None:
            c = cn.next
            cn.next = head
            head = cn
            cn = c
        cn.next = head
        head = cn
        return head