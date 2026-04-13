class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # target = image[sr][sc]
        # ROWS, COLS = len(image), len(image[0])
        
        # def bfs(r, c):
        #     q = collections.deque([(r,c)])
        #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #     while q:
        #         row, col = q.popleft()
        #         image[row][col] = color

        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc

        #             if r in range(ROWS) and c in range(COLS) and image[r][c] == target and image[r][c] != color:
        #                 q.append((r,c))
        # bfs(sr, sc)
        # return image
        if image[sr][sc] == color:
            return image
        target = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(r, c):
            if r == ROWS or r < 0 or c < 0 or c == COLS or image[r][c] != target or image[r][c] == color:
                return 
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image