class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        tree = PrefixTree()
        for word in words:
            tree.insert(word)

        res = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, path, node):
            if node.isEnd:
                res.append(("").join(path.copy()))
                node.isEnd = False
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] == "#" or board[i][j] not in node.children:
                return

            char = board[i][j]
            path.append(char)
            board[i][j] = "#"
            for x, y in directions:
                dfs(i + x, j + y, path, node.children[char])
            path.pop()
            board[i][j] = char
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, [], tree.root)
        return res

