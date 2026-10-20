class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        for k in range(1,n+1):
            if n%k!=0:
                continue
            valid=True
            prev_max=float('-inf')
            for i in range(0,n,k):
                block=nums[i:i+k]
                if prev_max>min(block):
                    valid=False
                    break
                count=0
                for j in range(k):
                    if block[j]>block[(j+1)%k]:
                        count+=1
                if count>1:
                    valid=False
                    break
                prev_max=max(block)
            if valid:
                ans+=k
        return ans