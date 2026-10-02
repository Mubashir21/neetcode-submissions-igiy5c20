# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        big, small = float('inf'), float('-inf')

        def dfs(root, small, big):
            if not root:
                return True
            if not (small < root.val < big):
                return False
            left = dfs(root.left, small, root.val)
            right = dfs(root.right, root.val, big)

            return left and right
        return dfs(root, small, big)