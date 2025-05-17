class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = list()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # 同じnums[i]をスキップ
            l, r = i+1, len(nums)-1 
            dif = 0 - nums[i]
            # print([nums[i], nums[l], nums[r]])
            while l < r:
                if nums[l] + nums[r] == dif:
                    triples.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                            l += 1
                    while l < r and nums[r] == nums[r+1]:
                            r -= 1
                elif nums[l] + nums[r] < dif:
                    l += 1
                elif nums[l] + nums[r] > dif:
                    r -= 1
        return triples
