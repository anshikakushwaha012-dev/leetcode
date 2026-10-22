class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        p=nums.index(0)
        if all(nums[(p+i)%n]==i for i in range(n)):
            return min(p,n-p+2) if p else 0
        p=nums.index(n-1)
        if all(nums[(p+i)%n]==n-1-i for i in range(n)):
            return min(p+1,n-p+1)
        return -1