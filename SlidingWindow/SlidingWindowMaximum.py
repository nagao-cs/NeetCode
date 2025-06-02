from collections import deque
from typing import List
VAL = 0
IDX = 1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r, n = 0, 0, len(nums) 
        num_repeat = n - k #numsの要素数とwindow_sizeの差だけwindowをずらす
        res = list()
        
        que = deque() #先頭から降順にする
        #最初の1回目
        for i in range(k):
            r = i
            num = nums[r]
            while que and que[-1][VAL] < num:
                que.pop()
            que.append((num, r))
        res.append(que[0][VAL])
        # print(f"(l, r):({l}, {r}), que:{que}")
        # print("↓")
        for _ in range(num_repeat):
            l, r = l+1, r+1 #windowをずらす
            num = nums[r]
            while que and que[-1][VAL] < num:
                que.pop()
            que.append((num, r))
            if que[0][IDX] < l:
                que.popleft()
            # print(f"(l, r):({l}, {r}), que:{que}")
            # print("↓")
            res.append(que[0][VAL])
        return res