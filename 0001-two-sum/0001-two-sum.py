class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        length=len(nums)
        for i in range(length):
            complement=target-nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]]=i

        
        