class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        from functools import lru_cache
        n = len(intervals)
        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))
        arr.sort()
        starts = [x[0] for x in arr]
        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect.bisect_right(starts, arr[i][1])
        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0:
                return (0, ())
            not_take = dp(i + 1, k)
            l, r, w, idx = arr[i]
            score, indices = dp(next_idx[i], k - 1)
            new_indices = tuple(sorted((idx,) + indices))
            take = (w + score, new_indices)
            if take[0] > not_take[0]:
                return take
            if take[0] < not_take[0]:
                return not_take
            return min(take, not_take)
        return list(dp(0, 4)[1])