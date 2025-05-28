from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        #positionが近い順にposition,speedソート
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort(key=lambda car: car[0], reverse=True)
        pos, sp = 0, 1
        numfleet = n

        arrival_stack = list()
        for car in cars:
            arrival_time = (target-car[pos])/car[sp]
            if (not arrival_stack) or (arrival_stack[-1] < arrival_time):
                arrival_stack.append(arrival_time)
            else:
                numfleet -= 1
        return numfleet