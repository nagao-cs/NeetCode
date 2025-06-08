class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        graphDict= dict() #オリジナルとコピーの対応関係を表す辞書

        def dfs(origin, copy):
            for neighbor in origin.neighbors:
                if neighbor in graphDict:
                    copy.neighbors.append(graphDict[neighbor])
                elif neighbor not in graphDict:
                    graphDict[neighbor] = Node(neighbor.val)
                    copy.neighbors.append(graphDict[neighbor])
                    dfs(neighbor, graphDict[neighbor])
        
        head = Node(node.val)
        graphDict[node] = head
        dfs(node, head)
        return head