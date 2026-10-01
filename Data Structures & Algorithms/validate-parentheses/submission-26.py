class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "]":"[", "}":"{"}
        stack = []

        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                if stack:
                    top = stack.pop()
                    if top == brackets[bracket]:
                        continue
                    else:
                        return False
                else:
                    return False
        return not stack