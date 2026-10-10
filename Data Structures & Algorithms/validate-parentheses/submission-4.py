class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for ele in s:
            if ele=='(' or ele=='{' or ele=='[':
                bracket_stack.append(ele)
                print(bracket_stack)

            if ele==')' or ele=='}' or ele==']':
                if len(bracket_stack) == 0:
                    return False
                else: 
                    if ele==')':
                        if bracket_stack[-1] == '(':
                            bracket_stack.pop(-1)
                        else:
                            return False
                    if ele=='}':
                        if bracket_stack[-1] == '{':
                            bracket_stack.pop(-1)
                        else:
                            return False
                    if ele==']':
                        if bracket_stack[-1] == '[':
                            bracket_stack.pop(-1)
                        else:
                            return False



        if len(bracket_stack) == 0:
            return True
        else: 
            return False
        