class Solution:
    def climbStairs(self, n: int) -> int:
        left, right = 1, 1

        for _ in range(n - 1):
            temp = right
            right = left + right
            left = temp
        return right