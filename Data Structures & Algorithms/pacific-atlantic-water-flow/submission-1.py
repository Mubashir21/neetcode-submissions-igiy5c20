class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        isPacific = set()
        isAtlantic = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(r, c, prev, islands):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in islands or heights[r][c] < prev:
                return

            islands.add((r, c))

            for nr, nc in dirs:
                dfs(nr + r, nc + c, heights[r][c], islands)
        
        for col in range(COLS):
            dfs(0, col, 0, isPacific)
            dfs(ROWS - 1, col, 0, isAtlantic)
        
        for row in range(ROWS):
            dfs(row, 0, 0, isPacific)
            dfs(row, COLS - 1, 0, isAtlantic)
        
        return list(isPacific & isAtlantic)