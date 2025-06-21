from collections import deque
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = {i: list() for i in range(n)}
        for i, j, price in flights:
            flight_dict[i].append((j, price))
        dp = [[0 if i == src else float('inf') for i in range(n)] for _ in range(k+1)]
        # dp[step][city]はsrcからstepでiへ行く場合の最安値
        
        que = deque()
        for next_city, price in flight_dict[src]:
            dp[0][next_city] = price
            que.appendleft(next_city)
        
        for step in range(1, k+1):
            for city in range(n):
                dp[step][city] = dp[step-1][city]

            for _ in range(len(que)):
                current_city = que.pop()
                for next_city, price in flight_dict[current_city]:
                    if dp[step-1][current_city] + price < dp[step][next_city]:
                        dp[step][next_city] = dp[step-1][current_city] + price
                        if next_city != dst:
                            que.appendleft(next_city)
            # for row in dp:
                # print(row)
            # print()

        if dp[k][dst] == float('inf'):
            return -1
        return int(dp[k][dst])