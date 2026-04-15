class Solution:
    def climbStairs(self, n: int) -> int:
        # left, right = 1, 1

        # for _ in range(n - 1):
        #     temp = right
        #     right = left + right
        #     left = temp
        # return right

        map = {}
        def dfs(stair):
            if stair == n:
                return 1
            if stair > n:
                return 0
            if stair in map:
                return map[stair]
            
            map[stair] = dfs(stair + 1) + dfs(stair + 2)
            return map[stair]
        return dfs(0)