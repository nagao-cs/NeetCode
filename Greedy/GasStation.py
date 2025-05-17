class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            if tank < 0:
                start = i+1
                tank = 0
        
        return start