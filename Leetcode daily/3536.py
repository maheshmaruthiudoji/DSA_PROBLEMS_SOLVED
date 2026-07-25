"""
3536. Maximum Product of Two Digits
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.
"""
class Solution:
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        digits.sort(reverse=True)
        return digits[0] * digits[1]