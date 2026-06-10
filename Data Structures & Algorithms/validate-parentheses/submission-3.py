from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False
        
        stack = deque()

        closed = {"]" : "[", "}": "{", ")" : "("}
        
        for char in s:
            if char in closed:
                if stack:
                    open = stack.pop()
                else:
                    return False
                if open != closed.get(char):
                    return False
            else:
                stack.append(char)

        return True if len(stack) == 0 else False