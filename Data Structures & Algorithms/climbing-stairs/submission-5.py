class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(stairs):
            if stairs < 0:
                return 0
            if stairs == 1:
                return 1
            if stairs == 2:
                return 2
            if stairs in mem:
                return mem[stairs]
            one = dfs(stairs - 1)
            two = dfs(stairs - 2)

            mem[stairs] = one + two
            return one + two
        return dfs(n)