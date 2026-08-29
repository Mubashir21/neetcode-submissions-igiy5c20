class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited or grid[i][j] != "1":
                return
            visited.add((i, j))
            for x, y in dirs:
                dfs(i + x, j + y)
            
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res