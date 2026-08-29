class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr=[]
        n=len(nums)
        nums.sort()
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            total_sum=-1*nums[i]
            while left<right:
                total=nums[left]+nums[right]
                if total==total_sum:
                    arr.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1
                    while (left<n and nums[left]==nums[left-1]):
                        left+=1
                    while (right>=0 and nums[right]==nums[right+1]):
                        right-=1
                else:
                    if total<total_sum:
                        left+=1
                    else:
                        right-=1
        return arr

                



        
