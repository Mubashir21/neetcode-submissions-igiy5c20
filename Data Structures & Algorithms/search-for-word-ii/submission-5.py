class TrieNode:
    def __init__(self):
        self.children = {}
        self.lastNode = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.lastNode = True

    def searchWord(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.lastNode

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j, node, path):
            if node.lastNode:
                res.add("".join(path.copy()))
        
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] not in node.children or board[i][j] == "#":
                return False
            
            char = board[i][j]
            board[i][j] = "#"
            path.append(char)

            for dr, dc in dirs:
                dfs(i + dr, j + dc, node.children[char], path)

            board[i][j] = char
            path.pop()

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, [])
        return list(res)



