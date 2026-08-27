class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        original=arr[:]
        ans=[]
        for i in range(len(original)):
            if original[i]==0:
                ans.append(0)
                ans.append(0)
            else:
                ans.append(original[i])
        arr[:]=ans[:len(arr)]