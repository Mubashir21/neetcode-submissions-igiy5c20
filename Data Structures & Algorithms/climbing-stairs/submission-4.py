class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(n):
            if n < 1:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in mem:
                return  mem[n]
            take = dfs(n - 1)
            skip = dfs(n - 2)

            mem[n] = take + skip
            return mem[n]
        return dfs(n)