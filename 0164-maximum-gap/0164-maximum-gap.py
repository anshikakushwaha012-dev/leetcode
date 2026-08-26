class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        answer=0
        for i in range(1,len(nums)):
            gap=nums[i]-nums[i-1]
            answer=max(answer,gap)
        return answer