class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        smallest_multiple=k
        while smallest_multiple in nums:
            smallest_multiple+=k
        return smallest_multiple