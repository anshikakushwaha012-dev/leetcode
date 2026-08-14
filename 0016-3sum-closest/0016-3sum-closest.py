class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cs=float('inf')
        for i in range(len(nums)-1):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if (abs(cs-target)> abs(total-target)):
                    cs=total
                if total>target:
                    right-=1
                elif total<target:
                    left+=1
                else:
                    return total
        return cs