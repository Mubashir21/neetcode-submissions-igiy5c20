class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            seen[s[r]] = 1 + seen.get(s[r], 0)

            if seen[s[r]] > 1:
                res = max(res, r - l)
                while seen[s[r]] > 1:
                    seen[s[l]] = seen.get(s[l]) - 1
                    l += 1
            r += 1
        
        return max(res, r - l)