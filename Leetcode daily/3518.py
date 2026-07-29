"""
You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 

Example 1:

Input: s = "abba", k = 2

Output: "baab"

Explanation:

The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
"""
from collections import Counter

class Solution:
    def smallestPalindrome(self, s, k):
        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        for c in cnt:
            if cnt[c] % 2:
                mid = c
            half[ord(c) - 97] = cnt[c] // 2

        n = sum(half)
        LIM = k

        def comb_limit(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            ans = 1
            for i in range(1, r + 1):
                ans = ans * (n - r + i) // i
                if ans > LIM:
                    return LIM + 1
            return ans

        def countWays(freq):
            rem = sum(freq)
            ans = 1
            for x in freq:
                if x:
                    ans *= comb_limit(rem, x)
                    if ans > LIM:
                        return LIM + 1
                    rem -= x
            return ans

        if countWays(half) < k:
            return ""

        left = []

        while sum(half):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                w = countWays(half)

                if w >= k:
                    left.append(chr(i + 97))
                    break
                else:
                    k -= w
                    half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]