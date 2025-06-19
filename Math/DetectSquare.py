from typing import List
class DetectSquares:

    def __init__(self):
        self.point_count = dict()
        self.hashmap = dict() #x -> list[y]

    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.hashmap:
            self.hashmap[x] = [y]
            self.point_count[(x, y)] = 1
        else:
            if y not in self.hashmap[x]:
                self.hashmap[x].append(y)
                self.point_count[(x, y)] = 1
            else:
                self.point_count[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        count = 0
        if x1 not in self.hashmap:
            return count
        for y2 in self.hashmap[x1]:
            # y_iは真下か真上の点、これが見つかっている
            length = abs(y1 - y2)
            if length == 0:
                continue
            for x2 in [x1-length, x1+length]:
                for diagonal_y in self.hashmap.get(x2, []):
                    if diagonal_y == y2:
                        # 条件を満たす対角の点が見つかった
                        for horizonal_y in self.hashmap.get(x2, []):
                            if horizonal_y == y1:
                                # print(f"[{x,y}], [{diagonal_x, diagonal_y}]")
                                count += (self.point_count[(x1, y2)]*self.point_count[(x2, y2)]*self.point_count[(x2, y1)])
        return count



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)