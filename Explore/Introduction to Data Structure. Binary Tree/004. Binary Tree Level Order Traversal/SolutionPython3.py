# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = [[]]
        p = deque()
        b = deque()
        l = 0
        c = root
        if c == None:
            return None
        p.append(c)
        b.append(l)
        while c != None or p:
            if c != None:
                if l == b[0]:
                    r[l].append(c.val)
                    p.append(c.left)
                    b.append(l+1)
                    p.append(c.right)
                    b.append(l+1)
                    p.popleft()
                    b.popleft()
                    c = p[0]
                else:
                    l = b[0]
                    r.append([])
            else:
                p.popleft()
                b.popleft()
                if p:
                    c = p[0]
        return r