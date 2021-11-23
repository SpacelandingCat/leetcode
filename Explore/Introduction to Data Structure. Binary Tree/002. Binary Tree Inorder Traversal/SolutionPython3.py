# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        p = []
        c = root
        while c != None or p:
            if c != None:
                if c.left != None or c.right != None:
                    p.append(c)
                else:
                    r.append(c.val)
                c = c.left
            else:
                c = p[-1]
                r.append(c.val)
                p.pop()
                c = c.right
        return r