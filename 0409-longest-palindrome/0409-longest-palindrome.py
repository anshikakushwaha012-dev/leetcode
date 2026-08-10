class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=0
        seen=set()
        for i in s:
            if i in seen:
                count+=2
                seen.remove(i)
            else:
                seen.add(i)
        if seen :
            count+=1
        return count

        