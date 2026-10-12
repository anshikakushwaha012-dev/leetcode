class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total=0
        for i in range(len(nums)):
            total+=nums[i]
        leftsum=0
        for i in range(len(nums)):
            rightsum=total-leftsum-nums[i]
            if(rightsum==leftsum):
                return i
            leftsum+=nums[i]
        return -1