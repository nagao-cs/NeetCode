class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 #i文字目からスタート
        ans = 0
        shift = 0
        while i < len(s):
            substring = list()
            j = 0 #i文字目からj文字目について
            while i+j < len(s):
                if s[i+j] not in substring:
                    substring += s[i+j]
                    j += 1
                else:
                    shift = 0
                    while substring[shift] != s[i+j]:
                        shift += 1
                    break
            if len(substring) > ans:
                ans = len(substring)
            i += shift+1
        return ans


