"""
Two Sum Problem
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Output: [0, 1]