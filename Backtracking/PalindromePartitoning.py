class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = list()
        """
        aabbaa
        [a,a,b,b,a,a],[aa,b,b,a,a],[aa,bb,a,a][aa,bb,aa],[aabbaa]
        """
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def backtrack(p: List[str], s: str) -> None:
            #pはpalindromeの文字列のリスト,sは残りの文字列
            if len(s) == 0:
                output.append(p[:])
            for i in range(1, len(s)+1):
                if is_palindrome(s[:i]):
                    #残りの文字をpalindromeになるように分割
                    p.append(s[:i])
                    backtrack(p, s[i:])
                    p.pop()
        
        backtrack(p=[], s=s)
        return output