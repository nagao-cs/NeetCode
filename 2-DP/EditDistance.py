from pprint import pprint
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = list()
        for i in range(m+1):
            if i == 0:
                dp.append([j for j in range(n+1)])
            else:
                dp.append([i if j == 0 else 0 for j in range(n+1)])
        # dp[i][j]はword1のi文字目まででword2のj文字目までを作るのに必要な操作の回数

        # pprint(dp)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j-1]

        # pprint(dp)

        return dp[-1][-1]