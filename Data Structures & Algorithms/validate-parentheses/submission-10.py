class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in "([{":
                stack.append(p)
            elif p == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif p == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif p == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        return not stack