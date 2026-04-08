class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}":"{", "]":"["}

        if len(s) == 1:
            return False

        stack = []

        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            elif stack:
                if stack[-1] != brackets[bracket]:
                    return False
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True