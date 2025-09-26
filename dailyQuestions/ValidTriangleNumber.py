from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def search_insert(nums, num):
            # numのほうが大きい数の中で最大のインデックスを探す
            l, r = 0, len(nums) - 1
            while l < r:
                pivot = (l+r)//2
                target = nums[pivot]
                if num <= target:
                    r = pivot - 1
                else:
                    l = pivot + 1
            if num > nums[l]:
                return l
            else:
                return l-1

        if len(nums) < 3:
            return 0
        
        nums.sort()
        i, j = 0, 1
        count = 0
        while i < len(nums) - 2:
            while j < len(nums) - 1:
                pivot = search_insert(nums, nums[i]+nums[j])
                # print(f"i={i}, j={j}, pivot={pivot}")
                count += max(pivot - j, 0)
                j += 1
            i += 1
            j = i + 1
        
        return count
