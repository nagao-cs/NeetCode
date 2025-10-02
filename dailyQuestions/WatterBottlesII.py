class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numEmpty = 0
        count = 0
        while numBottles:
            count += numBottles
            numEmpty += numBottles
            numBottles = 0
            if numEmpty >= numExchange:
                numEmpty -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                break
        
        return count