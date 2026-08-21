class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in nums:
            if i%2==0:
                arr.append(i)
        for i in nums:
            if i%2!=0:
                arr.append(i)
        return arr