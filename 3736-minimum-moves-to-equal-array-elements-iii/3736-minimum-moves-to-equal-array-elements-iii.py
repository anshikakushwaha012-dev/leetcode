class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        moves=0
        for i in range(len(nums)):
            moves+=maxi-nums[i]
        return moves