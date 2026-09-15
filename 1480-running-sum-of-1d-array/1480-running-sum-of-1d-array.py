class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            ans.append(sum)
        return ans
        