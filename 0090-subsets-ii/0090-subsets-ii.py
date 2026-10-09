class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[[]]
        start=0
        end=0
        for i in range(len(nums)):
            start=0
            if i>0 and nums[i]==nums[i-1]:
                start=end
            end=len(result)
            for j in range(start,end):
                result.append(result[j]+[nums[i]])
        return result