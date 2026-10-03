class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y, visited):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or (x, y) in visited or grid[x][y] == "0":
                return False
            
            visited.add((x, y))
            dfs(x + 1, y, visited)
            dfs(x, y + 1, visited)
            dfs(x - 1, y, visited)
            dfs(x, y - 1, visited)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c, visited)
                    res += 1
        return res
            