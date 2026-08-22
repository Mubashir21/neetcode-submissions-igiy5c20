class Solution:
    def isValid(self, s: str) -> bool:
        vocab = {"}":"{", "]":"[", ")":"("}
        stack = []

        for bracket in s:
            if bracket not in vocab:
                stack.append(bracket)
            else:
                if stack:
                    if stack.pop() != vocab[bracket]:
                        return False
                else:
                    return False
        return False if stack else True