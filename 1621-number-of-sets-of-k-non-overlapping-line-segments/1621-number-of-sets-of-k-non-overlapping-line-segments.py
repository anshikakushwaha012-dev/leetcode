class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD=10**9+7
        dp=[[0]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for j in range(1,k+1):
            total=0
            for i in range(1,n+1):
                if i>=2:
                    total+=dp[i-1][j-1]
                    total%=MOD
                dp[i][j]=(dp[i-1][j]+total)%MOD
        return dp[n][k]