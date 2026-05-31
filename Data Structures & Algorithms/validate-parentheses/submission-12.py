class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {')': '(', '}': '{', ']': '['}
        stack = []
        for bracket in s:
            if bracket in closedToOpen:
                # closed
                if stack and stack[-1] == closedToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                # open
                stack.append(bracket)
        return False if stack else True
