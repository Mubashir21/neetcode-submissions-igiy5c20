class Solution:
    def isValid(self, s: str) -> bool:
        maps = {")":"(", "}":"{", "]":"["}

        stack = []

        for bracket in s:
            if bracket in maps:
                if not stack:
                    return False
                
                opening = stack.pop()

                if opening != maps[bracket]:
                    return False
                
            else:
                stack.append(bracket)
        
        return len(stack) == 0