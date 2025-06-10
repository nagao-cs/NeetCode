import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = list() #大きい順にn//2個の要素を入れる
        self.maxHeap = list() #小さい順にn//2個の要素を入れる, #常にlen(maxHeap) >= len(minHeap)を維持する
        #[1,2,3,4,5] -> minHeap=[4,5], maxHeap=[3,1,2]
        self.size = 0

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, (-1)*num)
            self.size += 1
            return
        if num < (-1)*self.maxHeap[0]:
            heapq.heappush(self.maxHeap, (-1)*num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, (-1)*heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap)+1:
            heapq.heappush(self.minHeap, (-1)*heapq.heappop(self.maxHeap))
        self.size += 1

    def findMedian(self) -> float:
        # print(f"maxHeap:{self.maxHeap}")
        # print(f"minHeap:{self.minHeap}")
        # print()
        if self.size % 2 == 1:
            return float((-1)*self.maxHeap[0])
        else:
            return (self.minHeap[0] + (-1)*self.maxHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()