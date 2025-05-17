class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def make_heap(stones: List) -> list:
            heap = list()
            for stone in stones:
                insert_heap(heap, stone)
            return heap
        
        def insert_heap(heap: List, value: int) -> None:
            heap.append(value)
            current = len(heap)-1
            parent = (current-1)//2
            while current > 0 and heap[current] > heap[parent]:
                heap[current], heap[parent] = heap[parent], heap[current]
                current = parent
                parent = (current-1)//2
            
            return heap
        
        def pop_heap(heap: List) -> Optional[int]:
            if not heap:
                return None
            if len(heap) == 1:
                value = heap.pop()
                return value
            value = heap[0]
            heap[0] = heap.pop()
            current = 0
            while 2*current+1 < len(heap): #左には最低でも子がいる
                child_left, child_right = 2*current+1, 2*(current+1)
                if child_right >= len(heap): #右に子がいない
                    larger_child = child_left
                else: #どちらにも子がいる
                    if heap[child_left] > heap[child_right]:
                        larger_child = child_left
                    else:
                        larger_child = child_right
                if heap[current] < heap[larger_child]:
                    heap[current], heap[larger_child] = heap[larger_child], heap[current]
                else:
                    break
                current = larger_child
            
            return value
        
        heap = make_heap(stones)
        print(heap)
        while len(heap) > 1:
            y = pop_heap(heap)
            x = pop_heap(heap)
            if y-x > 0:
                insert_heap(heap, y-x)

        if heap:
            return heap.pop()
        else:
            return 0
