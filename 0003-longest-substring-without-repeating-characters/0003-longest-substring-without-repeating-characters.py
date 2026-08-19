class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        mapping = {}
        left = 0
        for right in range(len(s)):
            if s[right] in mapping:
                left = max(left, mapping[s[right]] + 1)
            mapping[s[right]] = right
            count = max(count, right - left + 1)
        return count
                


        
        
        