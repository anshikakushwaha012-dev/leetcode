class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = []
        for i in range(len(s)):
            arr.append((indices[i], s[i]))
        arr.sort()
        ans = ""
        for i in arr:
            ans += i[1]
        return ans