class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0 for _ in range(len(nums))] #最大値
        dp_min = [0 for _ in range(len(nums))] #最小値
        max_product = nums[0]

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp_max[i] = max(dp_max[i-1] * nums[i], nums[i])
                dp_min[i] = min(dp_min[i-1] * nums[i], nums[i])
            elif nums[i] < 0:
                dp_max[i] = max(dp_min[i-1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i-1] * nums[i], nums[i])
            elif nums[i] == 0:
                dp_max[i] = 0
                dp_min[i] = 0
            max_product = max(dp_max[i], max_product)
        
        return max_product