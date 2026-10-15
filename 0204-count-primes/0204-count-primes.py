class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[True]*n
        count=0
        for i in range(2,n):
            if prime[i]:
                count+=1
                for j in range(i*i,n,i):
                    prime[j]=False
        return count