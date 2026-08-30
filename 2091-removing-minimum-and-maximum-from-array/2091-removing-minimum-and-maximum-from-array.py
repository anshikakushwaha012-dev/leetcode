class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index=nums.index(min(nums))
        max_index=nums.index(max(nums))
        left=min(min_index,max_index)
        right=max(min_index,max_index)
        front=right+1
        back=len(nums)-left
        both=(left+1)+(len(nums)-right)
        return min(front,back,both) 