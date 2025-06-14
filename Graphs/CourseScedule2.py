from typing import List
from queue import Queue
class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.in_degree = set()
            self.out_degree = set()
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = dict()
        for i in range(numCourses):
            node = self.Node(i)
            nodes[i] = node
        for req in prerequisites:
            dst = req[0]
            src = req[1]
            nodes[src].out_degree.add(dst)
            nodes[dst].in_degree.add(src)
        
        que = Queue()
        delete = list()
        for key, node in nodes.items():
            if not node.in_degree:
                que.put(node)
                delete.append(key)
        for key in delete:
            del nodes[key]

        res = list()
        while not que.empty():
            node = que.get()
            res.append(node.val)
            for dst in node.out_degree:
                nodes[dst].in_degree.discard(node.val)
            delete = list()
            for key, node in nodes.items():
                if not node.in_degree:
                    que.put(node)
                    delete.append(key)
            for key in delete:
                del nodes[key]
        if nodes:
            return []
        return res           
