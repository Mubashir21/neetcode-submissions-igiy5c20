class Solution:
    def longestPalindrome(self, s: str) -> str:
        resString = ""
        resLen = 0

        for i in range(len(s)):

            r, l = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resString = s[l:r+1]
                l -= 1
                r += 1
        
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resString = s[l:r+1]
                l -= 1
                r += 1
        return resString