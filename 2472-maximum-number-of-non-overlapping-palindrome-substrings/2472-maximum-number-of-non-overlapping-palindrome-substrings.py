class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length == 2:
                        pal[left][right] = True
                    else:
                        pal[left][right] = pal[left + 1][right - 1]

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            for j in range(i):
                if i - j >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]