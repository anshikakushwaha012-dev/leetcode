class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+1):
            if i not in nums:
                arr.append(i)
        return arr
        