class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        left=0
        right=1
        while right<len(nums):
            if nums[right]==nums[left]:
                right+=1
            else:
                left+=1
                nums[left]=nums[right]
                right+=1
                count+=1
        return count
        