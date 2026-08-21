class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr=[]
        original=score.copy()
        score.sort()
        score=score[::-1]
        for i in range(len(score)):
            if i==0:
                arr.append("Gold Medal")
            elif i==1:
                arr.append("Silver Medal")
            elif i==2:
                arr.append("Bronze Medal")
            else:
                arr.append(str(i + 1))
        result=[]

        for x in original:
            result.append(arr[score.index(x)])
        return result