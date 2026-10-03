class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        isPacific = set()
        isAtlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(x, y, isOcean, prev):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or (x, y) in isOcean or prev > heights[x][y]:
                return
            
            isOcean.add((x, y))
            dfs(x+1, y, isOcean, heights[x][y])
            dfs(x, y+1, isOcean, heights[x][y])
            dfs(x-1, y, isOcean, heights[x][y])
            dfs(x, y-1, isOcean, heights[x][y])
        
        for r in range(ROWS):
            dfs(r, 0, isPacific, 0)
            dfs(r, COLS-1, isAtlantic, 0)

        for c in range(COLS):
            dfs(0, c, isPacific, 0)
            dfs(ROWS-1, c, isAtlantic, 0)
        
        return list(isAtlantic & isPacific)