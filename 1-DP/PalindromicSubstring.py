class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n
        # あきらめの2-DP
        dp = [[True if i == j else False for j in range(n)] for i in range(n)]

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        for length in range(3, n+1):
            for i in range(n-length+1):
                if dp[i+1][i+length-2] and s[i] == s[i+length-1]:
                    dp[i][i+length-1] = True
                    count += 1

        return count
