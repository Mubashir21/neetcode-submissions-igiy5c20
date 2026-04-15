class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        resLen, res = 0, ""

        # odd length string
        for i, char in enumerate(s):
            l = r = i
            print(i)
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                l-= 1
                r+= 1
        # even length string
        for i, char in enumerate(s):
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                l-= 1
                r+= 1
        return res