# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if self.dfs(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right

    def dfs(self, root, sub):
        if not root and not sub:
            return True
        
        if (not root and sub) or (root and not sub):
            return False
        
        if root.val != sub.val:
            return False
        
        left = self.dfs(root.left, sub.left) 
        right = self.dfs(root.right, sub.right) 

        return left and right

        