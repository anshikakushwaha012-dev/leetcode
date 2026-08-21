class Solution:
    def reverseWords(self, s: str) -> str:
        rev=""
        words=s.split()
        for word in words:
            for ch in word[::-1]:
                rev=rev + ch
            rev=rev + " "
        return rev.strip()