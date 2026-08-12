class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest=0
        for i in accounts:
            wealth=sum(i)
            richest=max(richest,wealth)
        return richest
        