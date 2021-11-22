"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        l = head
        p = []
        i = 0
        while l != None:
            if l.child != None:
                if l.next != None:
                    p.append(l.next)
                    i += 1
                l.next = l.child
                l.next.prev = l
                l.child = None
            else:
                if l.next == None and i > 0:
                    i -= 1
                    l.next = p[i]
                    l.next.prev = l
                    p.pop()
            l = l.next
        return head
