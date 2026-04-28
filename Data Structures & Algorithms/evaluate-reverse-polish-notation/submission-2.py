class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for c in tokens:
            if c in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if c == '+':
                    result = num1 + num2
                elif c == '-':
                    result = num1 - num2
                elif c == '*':
                    result = num1 * num2
                elif c == '/':
                    result = num1 / num2
                stack.append(result)
            else:
                stack.append(c)
        return int(stack[-1])