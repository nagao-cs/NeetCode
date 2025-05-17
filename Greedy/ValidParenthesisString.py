class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = list()
        star_stack = list()

        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)
            elif s[i] == ')':
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            else:
                star_stack.append(i)
        
        while open_stack:
            if len(open_stack) <= len(star_stack) and star_stack.pop() > open_stack.pop():
                continue
            else:
                return False
        return True