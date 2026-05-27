class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, visited, path):
            if ("").join(path) == word:
                return True
            if len(path) > len(word) or i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited:
                return False
            
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            path.append(board[i][j])
            visited.add((i, j))

            for dr, dc in directions:
                r, c = i + dr, j + dc
                if dfs(r, c, visited, path):
                    return True
            path.pop()
            visited.remove((i, j))
            # return False
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, set(), []):
                    return True
        return False