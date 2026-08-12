class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[]
        n=(len(nums)//2)
        left=0
        right=n
        for i in range(n):
            arr.append(nums[left])
            arr.append(nums[right])
            left+=1
            right+=1
        return arr


        