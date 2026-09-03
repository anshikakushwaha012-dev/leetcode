class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(num%2==0 for num in nums1):
            return True
        if all(num%2==1 for num in nums1):
            return True
        return min(nums1)%2==1