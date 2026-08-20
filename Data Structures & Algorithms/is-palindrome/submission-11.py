class Solution:
    def isPalindrome(self, s: str) -> bool:

        # a -> b is 97 -> 122
        # A -> B is 65 -> 90
        # 0 -> 9 is 48 -> 57

        l, r = 0, len(s) - 1

        while l <= r:
            while l <= r and not self.isType(s[l]):
                l += 1
            while l <= r and not self.isType(s[r]):
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def isType(self, char):
        if (97 <= ord(char) <= 122 or
            65 <= ord(char) <= 90 or
            48 <= ord(char) <= 57):
            return True
        return False