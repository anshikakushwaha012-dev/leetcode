class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = time % (2 * (n - 1))
        return t + 1 if t < n else 2 * n - 1 - t