class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endNode = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.endNode

            char = word[index]

            if char == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0, self.root)