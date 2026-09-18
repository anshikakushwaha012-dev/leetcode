class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        f=[len(s)]*26
        l=[-1]*26
        for i in range(len(s)):
            x=ord(s[i])-ord('a')
            f[x]=min(f[x],i)
            l[x]=i
        intervals=[]
        for i in range(len(s)):
            x=ord(s[i])-ord('a')
            if i!=f[x]:
                continue
            left=i
            right=l[x]
            j=left
            v=True
            while j<=right:
                y=ord(s[j])-ord('a')
                if f[y]<left:
                    v=False
                    break
                right=max(right,l[y])
                j+=1
            if v:
                intervals.append((left,right))
        intervals.sort(key=lambda x:x[1])
        arr=[]
        end=-1
        for left,right in intervals:
            if left>end:
                arr.append(s[left:right+1])
                end=right
        return arr