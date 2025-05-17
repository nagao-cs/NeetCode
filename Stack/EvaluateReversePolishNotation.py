class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(ope_1, ope_2, op):
            if op == '+':
                return ope_1 + ope_2
            elif op == '-':
                return ope_1 - ope_2
            elif op == '*':
                return ope_1 * ope_2
            elif op == '/':
                return ope_1 / ope_2
            else:
                raise SyntaxError
        ops = ['+', '-', '*', '/']
        stack = list()
        output = 0

        for token in tokens:
            if token in ops:
                ope_2 = stack.pop()
                ope_1 = stack.pop()
                res = calculate(ope_1, ope_2, token)
                stack.append(int(res))
            else:
                stack.append(int(token))
        
        return stack.pop()