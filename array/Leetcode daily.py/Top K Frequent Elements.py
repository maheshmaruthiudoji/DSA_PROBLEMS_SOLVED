"""
You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].

For each queries[i], extract the substring s[li..ri]. Then, perform the following:

Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x. The answer is x * sum.
Return an array of integers answer where answer[i] is the answer to the ith query.

Since the answers may be very large, return them modulo 109 + 7.
"""
class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7

        from bisect import bisect_left, bisect_right

        pos = []
        digit = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digit.append(ord(ch) - 48)

        k = len(pos)

        pre = [0] * (k + 1)
        for i in range(k):
            pre[i + 1] = pre[i] + digit[i]

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        pref = [0] * (k + 1)
        for i in range(k):
            pref[i + 1] = (pref[i] * 10 + digit[i]) % MOD

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r)

            if L == R:
                ans.append(0)
                continue

            cnt = R - L
            x = (pref[R] - pref[L] * pow10[cnt]) % MOD
            sm = pre[R] - pre[L]
            ans.append((x * sm) % MOD)

        return ans