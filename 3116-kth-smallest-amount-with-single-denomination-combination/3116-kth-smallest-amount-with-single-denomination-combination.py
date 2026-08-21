class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x):
            total = 0
            n = len(coins)
            for mask in range(1, 1 << n):
                lcm_value = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm_value = math.lcm(lcm_value, coins[i])
                if bits % 2 == 1:
                    total += x // lcm_value
                else:
                    total -= x // lcm_value
            return total
        left = 1
        right = k * min(coins)
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left