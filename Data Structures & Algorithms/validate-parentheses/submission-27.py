class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "]":"[", "}":"{"}
        stack = []

        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != brackets[bracket]:
                    return False
        return not stack