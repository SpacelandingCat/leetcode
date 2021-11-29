# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if targetSum == root.val and root.right == None and root.left == None:
            return True
        if root.right != None:
            r = self.hasPathSum(root.right, targetSum - root.val)
        else:
            r = False
        if root.left != None:
            l = self.hasPathSum(root.left, targetSum - root.val)
        else:
            l = False
        if l or r:
            return True
        return False
