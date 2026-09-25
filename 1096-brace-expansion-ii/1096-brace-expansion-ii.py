class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n=len(expression)
        def parse(i):
            ans=set()
            current={""}
            while i<n and expression[i]!= '}':
                if expression[i]=='{':
                    inside,i=parse(i+1)
                    temp=set()
                    for a in current:
                        for b in inside:
                            temp.add(a+b)
                    current=temp
                elif expression[i]==',':
                    ans.update(current)
                    current={""}
                    i+=1
                else:
                    temp=set()
                    for x in current:
                        temp.add(x+expression[i])
                    current=temp
                    i+=1
            ans.update(current)
            if i<n and expression[i]=='}':
                i+=1
            return ans,i
        ans,_=parse(0)
        return sorted(ans)