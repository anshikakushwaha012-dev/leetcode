class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            distinct=[]
            for j in range(i,n):
                if nums[j] not in distinct:
                    distinct.append(nums[j])
                ans+=len(distinct)*len(distinct)
        return ans