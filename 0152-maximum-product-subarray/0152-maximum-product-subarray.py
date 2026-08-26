class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=nums[0]
        minimum=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            if x<0:
                maximum,minimum=minimum,maximum
            maximum=max(x,maximum*x)
            minimum=min(x,minimum*x)
            ans=max(ans,maximum)
        return ans