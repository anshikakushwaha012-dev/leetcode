class Solution:
    def minSwaps(self, nums):
        def digitSum(n):
            total=0
            while n>0:
                total+= n%10
                n//=10
            return total
        arr=sorted(nums,key=lambda x:(digitSum(x),x))
        pos={nums[i]: i for i in range(len(nums))}
        visited=[False]*len(nums)
        swaps=0
        for i in range(len(nums)):
            if visited[i] or arr[i]==nums[i]:
                continue
            j=i
            cycle=0
            while not visited[j]:
                visited[j]=True
                j=pos[arr[j]]
                cycle+=1
            swaps+=cycle-1
        return swaps
