class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = sorted(s)
        newT = sorted(t)

        return newS == newT