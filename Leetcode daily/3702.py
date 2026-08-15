"""
3702. Longest Subsequence With Non-Zero Bitwise XOR
You are given an integer array nums.

Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.
"""
class Solution:
    def longestSubsequence(self, nums):
        x = 0

        for num in nums:
            x ^= num

        if x:
            return len(nums)

        return len(nums) - 1 if any(nums) else 0