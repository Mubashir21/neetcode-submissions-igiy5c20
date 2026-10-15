class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        dp = [[0] * n for _ in range(m)]
        
        def dfs(x, y):
            if (x, y) == (m-1, n-1):
                return 1
            if x < 0 or y < 0 or x >= ROWS or y >= COLS:
                return 0
            if dp[x][y] != 0:
                return dp[x][y]
            steps = 0
            steps += dfs(x, y+1)
            steps += dfs(x+1, y)
            dp[x][y] = steps

            return steps
        return dfs(0, 0)