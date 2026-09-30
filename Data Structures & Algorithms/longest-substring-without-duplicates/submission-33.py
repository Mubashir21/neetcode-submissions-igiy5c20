class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        l  = 0
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            if seen[s[i]] > 1:
                while seen[s[i]] > 1:
                    seen[s[l]] -= 1
                    l += 1
                seen[s[i]] = 1
            else:
                res = max(res, i - l + 1)
        return res


                
                