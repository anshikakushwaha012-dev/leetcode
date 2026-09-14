class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum=0
        sum=0
        for i in range(len(gain)):
            sum+=gain[i]
            maximum=max(maximum,sum)
        return maximum