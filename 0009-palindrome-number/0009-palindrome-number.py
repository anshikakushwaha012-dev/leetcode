class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr=list(str(x))
        arr1=arr[::-1]
        if arr1==arr:
            return True
        else:
            return False

        