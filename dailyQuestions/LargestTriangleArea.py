from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0

        for i in range(len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    vec_a = (points[j][0] - points[i][0], points[j][1] - points[i][1])
                    vec_b = (points[k][0] - points[i][0], points[k][1] - points[i][1])
                    area = abs(vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0]) / 2
                    # print(f"(i, j, k) = ({i}, {j}, {k})  area = {area}")
                    max_area = max(max_area, area)

        return max_area