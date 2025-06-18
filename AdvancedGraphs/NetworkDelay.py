import heapq
from typing import List
class Solution:
    class Node:
        def __init__(self, label):
            self.label = label
            self.adjacent = list()
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodedict = dict()
        for src, dst, time in times:
            if src not in nodedict:
                nodedict[src] = self.Node(src)
            if dst not in nodedict:
                nodedict[dst] = self.Node(dst)
            
            srcnode = nodedict[src]
            dstnode = nodedict[dst]
            srcnode.adjacent.append((dstnode, time))
        
        def dijkstra(start):
            visitTime = {label: float('inf') for label in range(1, n+1)}
            visitTime[start] = 0
            minHeap = list()
            heapq.heappush(minHeap, (0, start))

            while minHeap:
                cost, current = heapq.heappop(minHeap)
                if cost > visitTime[current]:
                    continue
                
                for next_node, weight in nodedict[current].adjacent:
                    new_cost = cost + weight
                    if new_cost < visitTime[next_node.label]:
                        visitTime[next_node.label] = new_cost
                        heapq.heappush(minHeap, (new_cost, next_node.label))
            return visitTime
        visitTime = dijkstra(k)
        minTime = max(visitTime.values())
        return int(minTime) if minTime != float('inf') else -1