class Solution:
    def isValid(self, s: str) -> bool:
        maps = {")":"(", "}":"{", "]":"["}

        stack = []

        for bracket in s:
            if bracket in maps and stack:
                opening = stack.pop()
                if opening != maps[bracket]:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True