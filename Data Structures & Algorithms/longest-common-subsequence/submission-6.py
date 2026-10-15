class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = [[-1] * len(text2) for _ in range(len(text1))]

        def dfs(i, j):
            if j == len(text2) or i == len(text1):
                return 0
            if mem[i][j] != -1:
                return mem[i][j]
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            
            res = max(dfs(i, j + 1), dfs(i + 1, j))
            mem[i][j] = res
            return res
        return dfs(0, 0)