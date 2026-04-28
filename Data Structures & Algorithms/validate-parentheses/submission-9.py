class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {')':'(', '}':'{', ']': '['}
        stack = []
        for p in s:
            if p in closedToOpen:
                # a closing parenthesis is reached
                if stack and closedToOpen[p] == stack[-1]:
                    # a valid pair
                    stack.pop()
                else:
                    return False
            else:
                # we are still on open parenthesis
                stack.append(p)
        return True if not stack else False 
