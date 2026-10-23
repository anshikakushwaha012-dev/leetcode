class Solution:
    def balancedString(self, s: str) -> int:
        n=len(s)
        k=n//4
        count={c: s.count(c) for c in "QWER"}
        if all(count[c]==k for c in count):
            return 0
        left=0
        ans=n
        for right in range(n):
            count[s[right]]-=1
            while all(count[c]<=k for c in count):
                ans=min(ans,right-left+1)
                count[s[left]]+=1
                left+=1
        return ans