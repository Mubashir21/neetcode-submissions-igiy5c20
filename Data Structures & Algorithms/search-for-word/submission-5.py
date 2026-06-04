class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        target = len(word)
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, index):
            if index == target:
                return True
            
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] == "#" or board[i][j] != word[index]:
                return False

            board[i][j] = "#"

            for dr, dc in steps:
                if dfs(i + dr, j + dc, index + 1):
                    return True
            board[i][j] = word[index]
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False