class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD=10**9+7
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][0]=dp[i][i]=1
        for i in range(2,n):
            for j in range(1,i):
                dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%MOD
        def solve(arr):
            if len(arr)<=2:
                return 1
            left=[x for x in arr if x<arr[0]]
            right=[x for x in arr if x>arr[0]]
            return(dp[len(arr)-1][len(left)] *
                    solve(left)*solve(right))%MOD
        return (solve(nums)-1)%MOD