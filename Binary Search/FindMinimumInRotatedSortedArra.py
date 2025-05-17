class Solution:
    def findMin(self, nums: List[int]) -> int:
        # print(nums)
        if len(nums) == 1:
            return nums[0]
        mid = len(nums)//2
        last = len(nums) - 1
        if mid == last: #要素が２つなら小さい方
            return min(nums)
        if nums[0] < nums[mid] < nums[last]: #順番通りなら先頭を返す
            return nums[0]
        else:
            if nums[0] < nums[mid] and nums[mid] > nums[last]:
                return self.findMin(nums[mid+1:])
            elif nums[0] > nums[mid]:
                return self.findMin(nums[:mid+1])
