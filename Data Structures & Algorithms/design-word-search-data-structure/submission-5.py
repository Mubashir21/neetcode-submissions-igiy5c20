class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(cur, index):
            if index == len(word):
                return cur.isEnd
            
            char = word[index]
            if char == ".":
                for child in cur.children:
                    if dfs(cur.children[child], index + 1):
                        return True
                return False
            else:
                if char not in cur.children:
                    return False
                return dfs(cur.children[char], index + 1)
        return dfs(self.root, 0)