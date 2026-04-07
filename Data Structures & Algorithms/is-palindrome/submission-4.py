class Solution:
    def isPalindrome(self, s: str) -> bool:
        validString = ""
        for ch in s:
            if ch.isalnum():
                validString += ch.lower()
        l, r = 0, len(validString) - 1
        while l <= r:
            if validString[l] != validString[r]:
                return False
            l += 1
            r -= 1
        return True