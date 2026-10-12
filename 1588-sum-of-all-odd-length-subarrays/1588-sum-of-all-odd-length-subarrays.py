
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        for i in range(n):
            for length in range(1,n-i+1,2):
                ans+=sum(arr[i:i+length])
        return ans