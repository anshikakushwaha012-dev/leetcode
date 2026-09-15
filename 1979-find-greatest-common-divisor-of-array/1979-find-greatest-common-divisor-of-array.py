class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest=float('inf')
        largest=-float('inf')
        for i in range(len(nums)):
            if nums[i]<smallest:
                smallest=nums[i]
            if nums[i]>largest:
                largest=nums[i]
        while largest!=0:
            smallest,largest=largest,smallest%largest
        return smallest    
                
        