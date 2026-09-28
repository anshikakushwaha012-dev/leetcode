class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        ans=0
        for i in s:
            if i=='(':
                depth+=1
                ans=max(ans,depth)
            elif i==')':
                depth-=1
        return ans