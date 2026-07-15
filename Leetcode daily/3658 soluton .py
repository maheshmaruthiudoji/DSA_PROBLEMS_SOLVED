"""
3658. GCD of Odd and Even Sums
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the smallest n positive odd numbers.

sumEven: the sum of the smallest n positive even numbers.

Return the GCD of sumOdd and sumEven

"""
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return gcd(n*n, n*(n+1))