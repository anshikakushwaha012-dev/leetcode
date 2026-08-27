class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=[0] *(len(nums)+1)
        for i in range(len(nums)):
            count[nums[i]]+=1
        duplicate=0
        missing=0
        for i in range(1,len(nums)+1):
            if count[i]==2:
                duplicate=i
            if count[i]==0:
                missing=i
        return [duplicate,missing]