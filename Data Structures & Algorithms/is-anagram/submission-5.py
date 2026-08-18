class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = 1 + count.get(char, 0)

        for i in range(len(t)):
            if t[i] not in count or count[t[i]] <= 0:
                return False
            count[t[i]] = count.get(t[i]) - 1
        return True