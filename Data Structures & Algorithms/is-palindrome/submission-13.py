class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:

            while not self.isAlnum(s[l]) and l < r:
                l += 1
            while not self.isAlnum(s[r]) and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isAlnum(self, char):
        if (ord('a') <= ord(char) <= ord("z") or
            ord("A") <= ord(char) <= ord("Z") or
            ord("0") <= ord(char) <= ord("9")
        ):
            return True
        else:
            return False