from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for num in nums[1:]:
            if num > dp[-1]:
                dp.append(num)
            else:
                l, r = 0, len(dp)-1
                while l < r:
                    mid = (l+r)//2
                    if num > dp[mid]:
                        l = mid+1
                    elif num == dp[mid]:
                        l = mid
                        break
                    else:
                        r = mid
                # del dp[l:]
                dp[l] = min(num, dp[l])
            # print(f"num:{num}, {dp}")
        
        return len(dp)
