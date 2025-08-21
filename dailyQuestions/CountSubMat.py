from pprint import pprint

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        output = 0
        
        nums = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            if mat[row][0] == 1:
                nums[row][0] = 1
            for col in range(1, n):
                if mat[row][col] == 1:
                    nums[row][col] = nums[row][col-1] + 1
                else:
                    nums[row][col] = 0
        # print(nums)
        
        for row in range(m):
            for col in range(n):
                # mat[row][col]を右下とする長方形を考える
                # 長方形の幅は1~nums[row][col]まで
                # 幅がwの時、高さは1~h (nums[i][j] >= w)
                if nums[row][col] == 0:
                    continue
                for width in range(1, nums[row][col]+1):
                    # print(f"row:{row}")
                    for height in range(row, -1, -1):
                        # print(f"width:{width}, height:{height}")
                        if nums[height][col] >= width:
                            output += 1
                        else:
                            break
        
        return output