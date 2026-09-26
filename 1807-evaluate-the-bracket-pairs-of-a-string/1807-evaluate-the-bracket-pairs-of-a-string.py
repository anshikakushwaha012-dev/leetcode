class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}
        for key, value in knowledge:
            d[key]=value
        answer=""
        i=0
        while i<len(s):
            if s[i]=='(':
                j=i+1
                while s[j]!=')':
                    j+=1
                key=s[i+1:j]
                if key in d:
                    answer+=d[key]
                else:
                    answer+="?"
                i=j+1
            else:
                answer+=s[i]
                i+=1
        return answer