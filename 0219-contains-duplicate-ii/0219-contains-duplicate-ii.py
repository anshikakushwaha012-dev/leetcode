class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping={}
        n=len(nums)
        for i in range (n):
            if nums[i] in mapping:
                if i - mapping[nums[i]] <=k:
                    return True
            mapping[nums[i]]=i 
        return False

        