class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, path):
            if ("").join(path) == word:
                return True
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] == "#":
                return False
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            path.append(board[i][j])
            board[i][j] = "#"
            for x, y in direction:
                if dfs(i + x, j + y, path):
                    return True
            char = path.pop()
            board[i][j] = char
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, []):
                    return True
        return False