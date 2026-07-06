"""
LeetCode 14: Longest Common Prefix

Problem:
Given an array of strings, find the longest common prefix among them.
If there is no common prefix, return an empty string.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"

Time Complexity: O(n × m)
Space Complexity: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


# Example
if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))