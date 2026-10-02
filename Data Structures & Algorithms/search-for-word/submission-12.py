class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(x, y, index):
            if index == len(word):
                return True
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or board[x][y] == "#" or board[x][y] != word[index]:
                return False

            for r, c in dirs:
                xr, yc = x + r, y + c
                tmp = board[x][y]
                board[x][y] = "#"
                if dfs(xr, yc, index + 1):
                    board[x][y] = tmp
                    return True
                board[x][y] = tmp
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

