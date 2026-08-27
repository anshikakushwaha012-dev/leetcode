class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total=0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if i%3==2:
                continue
            total=total+cost[i]
        return total