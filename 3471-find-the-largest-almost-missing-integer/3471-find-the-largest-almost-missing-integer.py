class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = [0] * 51
        for i in range(len(nums) - k + 1):
            seen = set()
            for j in range(i, i + k):
                seen.add(nums[j])
            for num in seen:
                count[num] += 1
        ans = -1
        for num in range(51):
            if count[num] == 1:
                ans = num
        return ans