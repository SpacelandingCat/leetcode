# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricRecursively(root.right, root.left)
        
    def isSymmetricRecursively(self, rroot: Optional[TreeNode], lroot: Optional[TreeNode]) -> bool:
        if rroot == None and lroot == None:
            return True
        if rroot != None and lroot != None:
            if rroot.right != None or rroot.left != None or lroot.right != None or lroot.left != None:
                if self.isSymmetricRecursively(rroot.right, lroot.left) and self.isSymmetricRecursively(rroot.left, lroot.right):
                    if rroot.val == lroot.val:
                        return True
            else:
                if rroot.val == lroot.val:
                    return True
        return False
        
    def isSymmetricIteratively(self, root: Optional[TreeNode]) -> bool:
        r = []
        p = []
        c = root.right
        while c != None or p:
            if c != None:
                r.append(c.val)
                if c.left != None or c.right != None:
                    p.append(c)
                c = c.left
            else:
                r.append(None)
                c = p[-1]
                c = c.right
                p.pop()
        l = []
        p = []
        c = root.left
        while c != None or p:
            if c != None:
                l.append(c.val)
                if c.left != None or c.right != None:
                    p.append(c)
                c = c.right
            else:
                l.append(None)
                c = p[-1]
                c = c.left
                p.pop()
        i = 0
        re = len(r)
        le = len(l)
        if re == le:
            while i < re:
                if r[i] != l[i]:
                    return False
                i += 1
            return True
        else:
            return False