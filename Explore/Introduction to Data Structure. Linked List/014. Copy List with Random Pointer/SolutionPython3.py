"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        sc = Node(head.val)
        c = sc
        p = {}
        p[head] = c
        if head.next != None:
            l = head.next
        else:
            l = None
        while l != None:
            n = Node(x=l.val)
            c.next = n
            c = n
            p[l] = c
            l = l.next
        c = sc
        l = head
        while l != None:
            if l.random != None:
                c.random = p[l.random]
            l = l.next
            c = c.next
        return sc
