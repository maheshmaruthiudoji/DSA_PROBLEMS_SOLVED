"""
3345. Smallest Divisible Digit Product I
You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.
"""
class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            product = 1
            temp = n

            while temp > 0:
                digit = temp % 10
                product *= digit
                temp //= 10

            if product % t == 0:
                return n

            n += 1