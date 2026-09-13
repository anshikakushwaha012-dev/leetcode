class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            answer=0
            while n>0:
                last_digit=n%10
                answer=answer+last_digit*last_digit
                n=n//10
            n=answer
        return True