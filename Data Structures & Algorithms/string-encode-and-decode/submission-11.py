class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            size = len(word)
            res += f"{size}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []

        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            number = int(s[l:r])
            
            word = s[r + 1:r + 1 + number]
            res.append(word)
            l = r + number + 1
        return res

