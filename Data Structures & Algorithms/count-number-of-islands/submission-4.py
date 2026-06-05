class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        count = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen or grid[r][c] != "1":
                return 

            seen.add((r, c))
            # grid[r][c] = "#"

            for nr, nc in dirs:
                dfs(r + nr, c + nc)
            # grid[r][c] = "1"

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count