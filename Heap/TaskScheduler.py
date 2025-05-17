from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def insert(heap: List[str], value: str) -> None:
            heap.append(value)
            current = len(heap) - 1
            while current > 0:
                parent = (current - 1) // 2
                if freq[heap[current]] > freq[heap[parent]]:
                    heap[current], heap[parent] = heap[parent], heap[current]
                    current = parent
                else:
                    break

        
        def pop(heap: List[str]) -> str:
            if len(heap) == 0:
                return None
            if len(heap) == 1:
                return heap.pop()
            poped = heap[0]
            heap[0] = heap.pop()
            current = 0
            while 2*current+1 < len(heap):
                if 2*(current+1) >= len(heap):
                    child = 2*current+1
                else:
                    if freq[heap[2*current+1]] < freq[heap[2*(current+1)]]:
                        child = 2*(current+1)
                    else:
                        child = 2*current+1
                
                if freq[heap[current]] < freq[heap[child]]:
                    heap[current], heap[child] = heap[child], heap[current]
                    current = child
                else:
                    break
            return poped
                    
        heap = list() #heapの一番上は最も優先度の高いタスク
        freq = Counter(tasks) #各タスクの出現頻度
        #ヒープの構成
        for task in freq:
            insert(heap, task)

        time = 0 #経過時間
        remain_task = len(freq) #残りタスク数
        while heap:
            cycle = set()
            time += 1
            task = pop(heap)
            freq[task] -= 1
            cycle.add(task)
            interval = 0
            while interval < n:
                if not heap:
                    break
                time += 1
                interval += 1
                task = pop(heap)
                freq[task] -= 1
                cycle.add(task)
            #heapの再構築
            for task in cycle:
                if freq[task] > 0:
                    insert(heap, task)
                else:
                    remain_task -= 1
            if interval < n:
                if remain_task == 0:
                    break
                else:
                    time += n - interval

        return time