class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(start,target,arr):
            if target==0:
                result.append(arr.copy())
                return
            for i in range(start,len(candidates)):
                if candidates[i]>target:
                    continue
                arr.append(candidates[i])
                backtrack(i,target-candidates[i],arr)
                arr.pop()
        backtrack(0,target,[])
        return result

