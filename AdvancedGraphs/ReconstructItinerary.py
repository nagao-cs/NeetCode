from typing import List
from pprint import pprint
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # pprint(graph)

        def dfs(current_city):
            # print(current_city)
            # オイラー路とHierholzer's Algorithm
            while graph[current_city]:
                next_city = graph[current_city].pop()
                dfs(next_city)
            itinerary.append(current_city)
            # pprint(itinerary)

            
        itinerary = list()
        dfs('JFK')
        return itinerary[::-1]