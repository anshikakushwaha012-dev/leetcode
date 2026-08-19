class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i=len(num)-1
        carry=k
        while i>=0:
            num[i]+=carry
            carry=num[i]//10
            num[i]%=10
            i-=1
            if carry==0:
                break
        while carry:
            num.insert(0,carry%10)
            carry//=10
        return num