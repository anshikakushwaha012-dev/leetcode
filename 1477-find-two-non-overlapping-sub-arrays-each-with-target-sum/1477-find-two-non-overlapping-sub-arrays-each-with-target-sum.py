class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        best=[100001]*n
        left=0
        total=0
        ans=100001
        for right in range(n):
            total+=arr[right]
            while total>target:
                total-=arr[left]
                left+=1
            if total==target:
                length=right-left+1
                if left>0 and best[left-1]!=100001:
                    ans=min(ans,length+best[left-1])
                if right==0:
                    best[right]=length
                else:
                    best[right]=min(best[right-1],length)
            else:
                if right>0:
                    best[right]=best[right-1]
        if ans==100001:
            return -1
        return ans