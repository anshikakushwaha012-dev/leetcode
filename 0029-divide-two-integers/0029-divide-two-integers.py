class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative=(dividend<0)!=(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        answer=0
        while dividend>=divisor:
            temp=divisor
            multiple=1
            while dividend>=(temp<<1):
                temp=temp<<1
                multiple=multiple<<1
            dividend-=temp
            answer+=multiple
        if negative:
            answer=-answer
        return min(max(answer,-2**31),2**31-1)
        
        