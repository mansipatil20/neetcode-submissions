class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                val1= stack.pop()
                val2=stack.pop()
                if i == '+':
                    stack.append(val1+val2)
                if i == '-':
                    stack.append(val2-val1)
                if i == '*':
                    stack.append(val1*val2)
                if i == '/':
                    stack.append(int(val2/val1))
        return stack[-1] if stack else -1