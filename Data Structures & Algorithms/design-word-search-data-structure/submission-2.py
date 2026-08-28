class TrieNode:
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
        def dfs(node, index):
            if index >= len(word):
                return node.isEnd
            
            char = word[index]

            if char == ".":
                for children in node.children.values():
                    if dfs(children, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                else:
                    return dfs(node.children[char], index + 1)
        return dfs(self.root, 0)