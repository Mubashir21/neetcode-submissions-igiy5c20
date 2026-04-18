class Solution:
    def numDecodings(self, s: str) -> int:
        maps = {}

        def dfs(i):
            if i in maps:
                return maps[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            ways = dfs(i + 1)

            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)
            maps[i] = ways

            return maps[i]
        return dfs(0)