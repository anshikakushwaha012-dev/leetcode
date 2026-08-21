class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        while columnNumber > 0:
            columnNumber -= 1
            arr.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(arr[::-1])