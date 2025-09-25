"""
1. Two Sum
작성일: 2025년 9월 26일

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        # Brute Force1: O(n^2) time | O(1) space
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # Brute Force2: O(n^2) time | O(1) space
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in nums[idx+1:]:
                output = [idx, nums[:].index(remain, idx+1)]
                return output
        """

        # Hash Map: O(n) time | O(n) space
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []  # Just in case there is no solution, though the problem guarantees one.



# Test cases
s = Solution()

# Example 1: nums = [2,7,11,15], target = 9
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = s.twoSum(nums1, target1)
print(f"Example 1:")
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {result1}")
print(f"Expected: [0,1]")
print(f"Correct: {result1 == [0, 1] or result1 == [1, 0]}")
print()

# Example 2: nums = [3,2,4], target = 6
nums2 = [3, 2, 4]
target2 = 6
result2 = s.twoSum(nums2, target2)
print(f"Example 2:")
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {result2}")
print(f"Expected: [1,2]")
print(f"Correct: {result2 == [1, 2] or result2 == [2, 1]}")
print()

# Example 3: nums = [3,3], target = 6
nums3 = [3, 3]
target3 = 6
result3 = s.twoSum(nums3, target3)
print(f"Example 3:")
print(f"Input: nums = {nums3}, target = {target3}")
print(f"Output: {result3}")
print(f"Expected: [0,1]")
print(f"Correct: {result3 == [0, 1] or result3 == [1, 0]}")
print()
