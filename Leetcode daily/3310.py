"""
3310. Remove Methods From Project

You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.
"""
from collections import deque

class Solution:
    def remainingMethods(self, n, k, invocations):
        g = [[] for _ in range(n)]

        for u, v in invocations:
            g[u].append(v)

        vis = [0] * n
        q = deque([k])
        vis[k] = 1

        while q:
            x = q.popleft()
            for y in g[x]:
                if not vis[y]:
                    vis[y] = 1
                    q.append(y)

        for u, v in invocations:
            if vis[v] and not vis[u]:
                return list(range(n))

        return [i for i in range(n) if not vis[i]]