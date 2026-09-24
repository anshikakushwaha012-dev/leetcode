class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            num=nums[i]
            sum=0
            while num>0:
                sum+=num%10
                num//=10
            if sum==i:
                return i
        return -1