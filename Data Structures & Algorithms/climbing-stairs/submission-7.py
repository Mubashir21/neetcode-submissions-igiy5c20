class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(stair):
            if stair == n:
                return 1
            if stair > n:
                return 0
            if stair in mem:
                return mem[stair]
            one = dfs(stair + 1)
            two = dfs(stair + 2)
            result = one + two
            mem[stair] = result
            return mem[stair]
        return dfs(0)
            