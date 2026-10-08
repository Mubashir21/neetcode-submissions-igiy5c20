class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}

        def dfs(index):
            if index == len(s):
                return True
            if index in mem:
                return mem[index]

            res = False
            for word in wordDict:
                if index + len(word) <= len(s) and s[index:index+len(word)] == word:
                    res =  res or dfs(index + len(word))
            mem[index] = res
            return mem[index]
        return dfs(0)