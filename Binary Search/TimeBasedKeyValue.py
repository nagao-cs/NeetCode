TIME=0
VALUE=1
class TimeMap:

    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timemap:
            self.timemap[key] = [(timestamp, value)]
        else:
            self.timemap[key].append((timestamp, value))
        # print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timemap:
            return ''
        idx = -1
        t_val_pair = self.timemap[key]
        l, r = 0, len(t_val_pair)-1
        # mid = (r+l)//2 として
        # t_val_pair[mid][TIME] < timestamp なら idx = midと仮置きして、l = mid+1として右側を探索
        # t_val_pair[mid][TIME] == timestamp なら idx = midで確定
        # t_val_pair[mid][TIME] > timestamp なら r = mid-1で左側を探索
        while l <= r:
            mid = (l+r)//2
            if t_val_pair[mid][TIME] < timestamp:
                idx = mid
                l = mid+1
            elif t_val_pair[mid][TIME] == timestamp:
                idx = mid
                break
            else:
                r = mid-1
        
        if idx == -1:
            return ''
        else:
            return self.timemap[key][idx][VALUE]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)