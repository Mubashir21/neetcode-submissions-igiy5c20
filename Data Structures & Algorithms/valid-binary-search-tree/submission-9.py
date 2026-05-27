# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        smallest, biggest = float("-inf"), float("inf")

        return self.dfs(smallest, biggest, root)

    def dfs(self, smallest, biggest, root):
        if not root:
            return True
        
        if root.val <= smallest or root.val >= biggest:
            return False
        return self.dfs(smallest, root.val, root.left) and self.dfs(root.val, biggest, root.right)