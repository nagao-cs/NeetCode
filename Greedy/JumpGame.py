class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        #dp[i]はiまで移動できるか

        i = 0
        while i < len(nums):
            if not dp[i]:
                return False
            if dp[-1]: #最後までジャンプできるなら終了
                return True

            for j in range(nums[i]+1):
                if i + j < len(nums):
                    dp[i+j] = True
            i += 1

        return dp[len(nums)-1] 