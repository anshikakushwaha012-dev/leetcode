class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:x*x)
        ans=0
        n=len(nums)
        for i in range(n):
            if i<(n+1)//2:
                ans+=nums[n-1-i]*nums[n-1-i]
            else:
                ans-=nums[n-1-i]*nums[n-1-i]
        return ans