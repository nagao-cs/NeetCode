from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: (point[0], -point[1]))
        # print(points)

        x, y = 0, 1
        count = 0
        n = len(points)
        for i in range(n):
            A = points[i]
            for j in range(i+1, n):
                B = points[j]
                if A[y] < B[y]:
                    continue
                flag = True
                for k in range(i+1, j):
                    C = points[k]
                    if A[x] <= C[x] <= B[x] and A[y] >= C[y] >= B[y]:
                        flag = False
                        break  
                if flag:
                    # print(f"upper-left:{A}, lower-right:{B}")
                    count += 1
        
        return count