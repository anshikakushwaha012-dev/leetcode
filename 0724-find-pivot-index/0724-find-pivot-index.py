class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=0
        left=0
        for i in range(len(nums)):
            total+=nums[i]
        for i in range(len(nums)):
            right=total-nums[i]-left
            if left==right:
                return i
            left+=nums[i]
        return -1
        
            
        