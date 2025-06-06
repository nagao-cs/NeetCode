class Solution:
    def isHappy(self, n) -> bool:
        prev_set = set()
        while n not in prev_set:
            prev_set.add(n)
            tmp = 0
            n = str(n)
            for i in n:
                tmp += int(i)**2
            
            n = tmp
        
        return n == 1