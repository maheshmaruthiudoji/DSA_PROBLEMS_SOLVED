"""
3517. Smallest Palindromic Rearrangement I

You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.
"""
from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        freq = Counter(s)
        left = []
        middle = ""

        for ch in sorted(freq):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                middle = ch

        left = "".join(left)
        return left + middle + left[::-1]