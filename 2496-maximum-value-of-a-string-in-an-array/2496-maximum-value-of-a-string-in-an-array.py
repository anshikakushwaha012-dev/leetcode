class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        ans = 0

        for s in strs:
            if s.isdigit():
                value = int(s)
            else:
                value = len(s)

            ans = max(ans, value)

        return ans