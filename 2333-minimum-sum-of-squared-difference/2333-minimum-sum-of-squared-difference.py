class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        k = k1 + k2
        if sum(diff) <= k:
            return 0
        freq = [0] * 100001
        for d in diff:
            freq[d] += 1
        for d in range(100000, 0, -1):
            if k <= 0:
                break
            count = freq[d]
            if count == 0:
                continue
            next_count = freq[d - 1]
            cost = count
            if k >= cost:
                freq[d - 1] += count
                freq[d] = 0
                k -= cost
            else:
                reduce_by = k // count
                remainder = k % count
                freq[d] -= remainder
                freq[d - 1] += remainder
                target = d - reduce_by
                freq[target] += count - remainder
                freq[d] -= count - remainder
                k = 0
        ans = 0
        for d in range(100001):
            ans += d * d * freq[d]
        return ans