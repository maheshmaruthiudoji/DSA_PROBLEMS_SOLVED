"""
1081. Smallest Subsequence of Distinct Characters

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""
class Solution(object):
    def smallestSubsequence(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        stack = []
        visited = set()

        for ch in s:
            count[ch] -= 1

            if ch in visited:
                continue

            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)