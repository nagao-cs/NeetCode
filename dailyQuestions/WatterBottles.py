class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        numEmpty = 0
        while numBottles:
            count += numBottles
            numEmpty += numBottles
            numBottles = numEmpty // numExchange
            numEmpty = numEmpty % numExchange
            # print(numBottles)

        return count