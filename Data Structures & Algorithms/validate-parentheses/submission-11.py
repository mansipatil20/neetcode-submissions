class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        endp ={
            "}":"{",
            "]":"[",
            ")":"(",
        }
        
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in endp:
                if not stack:
                    return False
                opening = stack.pop()
                if opening != endp[c]:
                    return False         
        return len(stack)==0
        