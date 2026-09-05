class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        arr=[]
        wordlen=len(words[0])
        totalwords=len(words)
        count={}
        for i in words:
            count[i]=count.get(i,0)+1
        for i in range(wordlen):
            left=i
            right=i
            current={}
            used=0
            while right+wordlen<=len(s):
                i=s[right:right+wordlen]
                right+=wordlen
                if i not in count:
                    current={}
                    used=0
                    left=right
                    continue
                current[i]=current.get(i,0)+1
                used+=1
                while current[i]>count[i]:
                    leftword=s[left:left+wordlen]
                    current[leftword]-=1
                    left+=wordlen
                    used-=1
                if used==totalwords:
                    arr.append(left)
        return arr