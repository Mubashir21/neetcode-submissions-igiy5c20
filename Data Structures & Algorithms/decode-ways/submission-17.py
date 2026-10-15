class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}
        def dfs(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in mem:
                return mem[index]
            
            one = dfs(index + 1)
            two = 0
            if ((index + 2) <= len(s) and 
            (int(s[index:index+2]) >= 10 and 
            int(s[index:index+2]) < 27)):
               two = dfs(index + 2)
            mem[index] = one + two
            return mem[index]
        return dfs(0)