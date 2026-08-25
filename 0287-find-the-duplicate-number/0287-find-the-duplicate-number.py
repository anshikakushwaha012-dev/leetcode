class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        answer=0
        left=1
        for i in range(len(nums)):
            if nums[i]!= nums[left]:
                left+=1
            else:
                answer=nums[left]
        return answer
