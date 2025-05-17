class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        
        open_stack = list()

        for bracket in s:
            if bracket in brackets:
                open_stack.append(bracket)
                continue
            elif len(open_stack) == 0:
                return False
            open = open_stack.pop()
            if brackets[open] != bracket:
                return False
        if len(open_stack) != 0:
            return False
        return True
            
