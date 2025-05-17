class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX = 10**4+1
        dp = [MAX for _ in range(len(nums))]
        #dp[i]はそこまで何回のジャンプでいけるか
        dp[0] = 0
        
        for i in range(len(nums)):
            for distanse in range(nums[i]+1):
                current = i
                if current + distanse < len(nums):
                    dp[current+distanse] = min(dp[current+distanse], dp[current]+1)
            # print(dp)
        return dp[-1]
            
            
