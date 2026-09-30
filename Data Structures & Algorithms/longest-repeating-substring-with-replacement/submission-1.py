class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        seen = {}

        maxFreq = 0
        l = 0

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)

            maxFreq = max(maxFreq, seen[s[r]])

            while (r - l + 1) - maxFreq > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res