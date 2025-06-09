from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = Heap(capacity=k)
        for point in points:
            heap.insert(point)
        return heap.heap

#根が最大値のheap
class Heap:
    def __init__(self, capacity):
        self.heap = list()
        self.capacity = capacity
        self.size = 0
    
    def dist(self, point):
        x, y = point
        return (x**2 + y**2)**(0.5)

    def insert(self, point):
        if self.size >= self.capacity:
            #もうk個の点が入っているとき
            if self.dist(self.heap[0]) < self.dist(point):
                #ヒープの根(最大値)よりも入力が大きければ入れない
                return
            else:
                #最大値よりも小さいなら根を取り出して入れる
                self.pop()
        
        self.heap.append(point)
        self.size += 1
        current = len(self.heap)-1
        parent = (current-1)//2
        while (current > 0):
            #ヒープの根にたどり着くまで
            dist1 = self.dist(self.heap[current])
            dist2 = self.dist(self.heap[parent])
            if dist1 > dist2:
                #挿入する値の方が大きい
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
                parent = (current-1)//2
            else:
                break
    
    def pop(self):
        current = 0
        self.heap[0] = self.heap[self.size-1]
        self.heap.pop()
        self.size -= 1
        
        while self.size > 2*current + 1:
            left, right = 2*current + 1, 2*(current+1)
            if self.size-1 < right:
                child = left
            else:
                dist1 = self.dist(self.heap[left])
                dist2 = self.dist(self.heap[right])
                if dist1 > dist2:
                    #左の子の方が大きいなら左のこと比較する
                    child = left
                else:
                    #そうでなければ右のこと比較する
                    child = right
            
            dist1 = self.dist(self.heap[current])
            dist2 = self.dist(self.heap[child])
            if dist1 < dist2:
                #根に近い方が大きくなるように
                self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
                current = child
            else:
                break