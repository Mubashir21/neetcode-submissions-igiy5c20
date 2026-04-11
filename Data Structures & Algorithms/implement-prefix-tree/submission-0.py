class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self.node = self.root

        for char in word:
            if char not in self.node.children:
                self.node.children[char] = TrieNode()
            self.node = self.node.children[char]
        self.node.endNode = True

    def search(self, word: str) -> bool:
        self.node = self.root

        for char in word:
            if char not in self.node.children:
                return False
            self.node = self.node.children[char]
        return self.node.endNode

    def startsWith(self, prefix: str) -> bool:
        self.node = self.root

        for char in prefix:
            if char not in self.node.children:
                return False
            self.node = self.node.children[char]
        return True
        