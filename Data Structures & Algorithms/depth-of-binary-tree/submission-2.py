# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.dfs(root, 0)

    def dfs(self, root, count):
        if not root:
            return 0
        
        left = self.dfs(root.left, count + 1)
        right = self.dfs(root.right, count + 1)

        return 1 + max(left, right)