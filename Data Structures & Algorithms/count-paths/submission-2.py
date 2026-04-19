class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maps = {}
        ROWS, COLS = m, n

        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) in maps:
                return maps[(r, c)]
            
            maps[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return maps[(r, c)]
        return dfs(0, 0)