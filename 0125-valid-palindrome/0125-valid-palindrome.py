class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isalnum():
                ans +=ch.lower()
        rev=ans[::-1]
        if rev==ans:
            return True
        else:
            return False