class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product = 1
        total_sum = 0
        original = n
        while n > 0:
            last_digit = n % 10
            total_sum = total_sum + last_digit
            product = product * last_digit
            n = n // 10
        return original % (total_sum + product) == 0