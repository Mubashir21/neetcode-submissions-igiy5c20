class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {chr(i):i-65+1 for i in range(65, 65+26)}
        mem = {}
        
        def dfs(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in mem:
                return mem[index]
            
            one = dfs(index + 1)
            two = 0
            if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                two = dfs(index + 2)
            mem[index] = one + two
            return mem[index]
        return dfs(0)
        