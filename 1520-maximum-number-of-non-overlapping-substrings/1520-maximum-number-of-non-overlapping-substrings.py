class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [len(s)] * 26
        last = [-1] * 26
        for i in range(len(s)):
            x = ord(s[i]) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i
        intervals = []
        for i in range(len(s)):
            x = ord(s[i]) - ord('a')
            if i != first[x]:
                continue
            left = i
            right = last[x]
            j = left
            valid = True
            while j <= right:
                y = ord(s[j]) - ord('a')
                if first[y] < left:
                    valid = False
                    break
                right = max(right, last[y])
                j += 1
            if valid:
                intervals.append((left, right))
        intervals.sort(key=lambda x: x[1])
        ans = []
        end = -1
        for left, right in intervals:
            if left > end:
                ans.append(s[left:right + 1])
                end = right
        return ans