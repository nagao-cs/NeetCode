from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        i, j, k = 0, 1, 2
        largest = 0

        for i in range(len(nums)-2):
            if nums[i] >= nums[i+1] + nums[i+2]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] < largest:
                continue
            for j in range(i+1, len(nums)-1):
                for k in range(i+2, len(nums)):
                    if nums[i] < nums[j] + nums[k]:
                        if nums[i] + nums[j] + nums[k] > largest:
                            largest = nums[i] + nums[j] + nums[k]
                        else:
                            break
                    else:
                        break
            else:
                break
        
        return largest