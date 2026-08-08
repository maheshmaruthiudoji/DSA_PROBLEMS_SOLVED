"""
3302. Find the Lexicographically Smallest Valid Sequence

You are given two strings word1 and word2.

A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

A sequence of indices seq is called valid if:

The indices are sorted in ascending order.
Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.

Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.
"""
class Solution:
    def validSequence(self, word1, word2):
        n, m = len(word1), len(word2)

        suf = [0] * (n + 1)
        j = m - 1

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                suf[i] += 1
                j -= 1

        ans = []
        j = 0
        used = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not used and suf[i + 1] >= m - j - 1:
                ans.append(i)
                j += 1
                used = True

        return ans if j == m else []