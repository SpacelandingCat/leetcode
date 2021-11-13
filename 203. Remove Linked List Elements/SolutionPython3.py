# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode()
        p = result
        h = head
        if h:
            while h.next != None:
                if h.val != val:
                    p.next = ListNode()
                    p = p.next
                    p.val = h.val
                h = h.next
            if h.val != val:
                p.next = ListNode()
                p = p.next
                p.val = h.val
        return result.next