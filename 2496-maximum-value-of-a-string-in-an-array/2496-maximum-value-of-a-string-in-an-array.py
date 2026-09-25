class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        answer=0
        for s in strs:
            if s.isdigit():
                value=int(s)
            else:
                value=len(s)
            answer=max(answer,value)
        return answer