class Solution:
    def climbStairs(self, n: int) -> int:
        left, right = 0, 1
        
        for step in range(n):
            right, left = left + right, right
        return right
