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
    
    def searchPrefix(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tree = Trie()
        for word in words:
            tree.addWord(word)

        res = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] not in node.children or board[r][c] == "#":
                return 

            letter = board[r][c]
            word += letter
            board[r][c] = "#"
            node = node.children[letter]
            if node.lastNode:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            board[r][c] = letter
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, tree.root, "")
        return list(res)












        