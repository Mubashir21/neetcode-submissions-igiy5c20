class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        maps = {}

        def dfs(one, two):
            if one == len(text1) or two == len(text2):
                return 0
            
            if (one, two) in maps:
                return maps[(one, two)]
            
            if text1[one] == text2[two]:
                maps[(one, two)] = 1 + dfs(one + 1, two + 1)
            else:
                maps[(one, two)] = max(dfs(one + 1, two), dfs(one, two + 1))
            
            return maps[(one, two)]

        return dfs(0, 0)

        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        # return dp[0][0]