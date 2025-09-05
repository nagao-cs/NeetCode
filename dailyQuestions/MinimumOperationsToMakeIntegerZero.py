class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for n in range(1, 61):
            sub = num1 - (n * num2)
            if sub < n:
                return -1
            elif sub.bit_count() <= n:
                return n
        
        return -1