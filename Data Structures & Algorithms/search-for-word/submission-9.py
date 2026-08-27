class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] == "#" or board[i][j] != word[index]:
                return False
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            board[i][j] = "#"
            for x, y in direction:
                if dfs(i + x, j + y, index + 1):
                    return True
            board[i][j] = word[index]
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False