class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pacificSet = set()
        atlanticSet = set()

        def dfs(i, j, prev, visited):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or heights[i][j] < prev:
                return
            
            visited.add((i, j))
            
            for x, y in dirs:
                dfs(i + x, j + y, heights[i][j], visited)

        for r in range(ROWS):
            dfs(r, 0, 0, pacificSet)
            dfs(r, COLS - 1, 0, atlanticSet)

        for c in range(COLS):
            dfs(0, c, 0, pacificSet)
            dfs(ROWS - 1, c, 0, atlanticSet)
        
        return list(pacificSet & atlanticSet)