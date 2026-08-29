class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=[]
        n=len(numbers)
        left=0
        right=n-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                break
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        arr.append(left+1)
        arr.append(right+1)
        return arr
