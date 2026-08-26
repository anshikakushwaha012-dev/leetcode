class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        count=0
        ans=""
        for right in range(len(s)):
            if s[right]=='1':
                count+=1
            while count==k:
                cur=s[left:right + 1]
                if ans==""or len(cur)<len(ans):
                    ans=cur
                elif len(cur)==len(ans) and cur<ans:
                    ans=cur
                if s[left]=='1':
                    count-=1
                left+=1
        return ans