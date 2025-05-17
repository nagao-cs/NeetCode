class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        num_Open = 0
        num_Close = 0
        ans = list()

        def backtrack(s:str, numOpen:int, numClose:int):
            if len(s) == 2*n:
                ans.append(s)
                return
            if numOpen < n:
                #'('を追加できる
                backtrack(s+'(', numOpen+1, numClose)
            if numClose < numOpen:
                #')'を追加できる
                backtrack(s+')', numOpen, numClose+1)

        backtrack('', 0, 0)
        return ans
        
        '''
        n=1: "()"
        n=2: "()()", "(())"
        n=3: "((())), "(())()", "()(())", "(()())", "()()()"
        '''