class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        chars = {}

        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1

        for ch in t:

            if ch not in chars:
                return False
            if chars[ch] > 0:
                chars[ch] = chars.get(ch) - 1
            else:
                return False
        return True

