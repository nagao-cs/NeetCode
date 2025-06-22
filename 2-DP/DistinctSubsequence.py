class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s)+1, len(t)+1
        dp = [[0 if j != 0 else 1 for j in range(n)] for i in range(m)]
        #dp[i][j]はsのi文字目まで(s[:i])の部分文字列が作れるtのj文字目まで(t[:j])の数

        for i in range(1, m):
            for j in range(1, n):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
            # for row in dp:
                # print(row)
            # print()
        
        return dp[m-1][n-1]