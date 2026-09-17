class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        arr=[]
        while(left<right):
            if numbers[left]+numbers[right]==target:
                break
            elif(numbers[left]+numbers[right]<target):
                left+=1
            else:
                right-=1
        arr.append(left+1)
        arr.append(right+1)
        return arr
                