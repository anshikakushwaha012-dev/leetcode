class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer=0
        nums.sort()
        answer=sum(nums[::2])
        return answer
