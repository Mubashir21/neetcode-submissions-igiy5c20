class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Tree:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Tree()
        for word in words:
            tree.addWord(word)
        ROWS, COLS = len(board), len(board[0])
        dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]
        res = []

        def dfs(x, y, cur, path):
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS or board[x][y] == "#" 
            or board[x][y] not in cur.children):
                return False

            char = board[x][y]
            board[x][y] = "#"
            cur = cur.children[char]
            path.append(char)
            if cur.isEnd:
                res.append(("").join(path))
                cur.isEnd = False
            for r, c in dirs:
                dfs(x + r, y + c, cur, path)
            path.pop()
            board[x][y] = char
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, tree.root, [])
        return res