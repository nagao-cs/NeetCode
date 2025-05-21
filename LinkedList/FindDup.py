from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        bitmap = [0 for _ in range(n)]
        #bitmap[i]はi+1がnumsにでてきたかの判定
        for num in nums:
            if bitmap[num-1]:
                return num
            else:
                bitmap[num-1] = 1
        return 0
        
        