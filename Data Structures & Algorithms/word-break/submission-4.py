class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}

        def dfs(index):
            if index == len(s):
                return True
            if index in mem:
                return mem[index]

            for word in wordDict:
                if index + len(word) <= len(s) and s[index:index+len(word)] == word:
                    if dfs(index + len(word)):
                        mem[index] = True
                        return True
            mem[index] = False
            return False
        return dfs(0)