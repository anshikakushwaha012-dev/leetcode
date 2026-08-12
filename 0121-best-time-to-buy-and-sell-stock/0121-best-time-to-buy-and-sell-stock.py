class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue=prices[0]
        maxvalue=0
        result=0
        for i in range(len(prices)):
            if prices[i]<minvalue:
                minvalue=prices[i]
            maxvalue=prices[i]-minvalue
            if maxvalue>result:
                result=maxvalue
        
        return result
        