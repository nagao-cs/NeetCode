class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        dp_left = [0 for _ in range(length)]
        dp_right = [0 for _ in range(length)]

        dp_left[0] = nums[0]
        dp_right[length-1] = nums[length-1]
        for i in range(1, length):
            if nums[i] == 1:
                dp_left[i] = dp_left[i-1] + 1
            if nums[length-i-1] == 1:
                dp_right[length-i-1] = dp_right[length-i] + 1

        # print(f"dp_left:{dp_left}")
        # print(f"dp_right:{dp_right}")
        
        ans = dp_right[1]
        for i in range(1, length-1):
            ans = max(ans, dp_left[i-1]+dp_right[i+1])
        ans = max(ans, dp_left[length-2])
        return ans