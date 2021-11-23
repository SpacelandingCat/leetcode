# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        p = []
        b = []
        c = root
        while c != None or p:
            if c != None:
                if c.left != None or c.right != None:
                    if p and p[-1] == c:
                        if b[-1] == 0:
                            c = c.right
                            b[-1] = 1
                        else:
                            r.append(c.val)
                            p.pop()
                            b.pop()
                            if p:
                                c = p[-1]
                            else:
                                c = None
                    else:
                        p.append(c)
                        b.append(0)
                        c = c.left
                else:
                    r.append(c.val)
                    c = c.left
            else:
                c = p[-1]
        return r
