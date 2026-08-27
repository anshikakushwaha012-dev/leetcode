class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        count=Counter(s)
        n=len(s)
        for i in range(n-1,-1,-1):
            temp=Counter(s)
            possible=True
            for j in range(i):
                if temp[target[j]]>0:
                    temp[target[j]]-=1
                else:
                    possible=False
                    break
            if not possible:
                continue
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch>target[i] and temp[ch]>0:
                    temp[ch]-=1
                    answer=target[:i]+ch
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        answer+=c*temp[c]
                    return answer
        return ""