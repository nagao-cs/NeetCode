from typing import List
class Solution:
    class Node:
        def __init__(self, val:int, children=None):
            self.val = val
            self.children = children if children is not None else set()

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeDict = dict()
        for dst, src in prerequisites:
            if not dst in nodeDict:
                nodeDict[dst] = self.Node(val=dst)
            if not src in nodeDict:
                nodeDict[src] = self.Node(val=src)
            nodeDict[src].children.add(nodeDict[dst])
        # for val, node in nodeDict.items():
            # print(node.val, node.children)

        visited_all = set()
        visited = set()
        for src in nodeDict:
            node = nodeDict[src]
            if node not in visited_all:
                if self.cycleCheck(node, visited, visited_all):
                    return False
        
        return True
    
    def cycleCheck(self, node, visited, visited_all) -> bool:
        # print(node.val, visited)
        if node in visited:
            return True
        if node in visited_all:
            return False

        visited.add(node)
        for dst in node.children:
            if self.cycleCheck(dst, visited, visited_all):
                return True
        
        visited.discard(node)
        visited_all.add(node)

        return False