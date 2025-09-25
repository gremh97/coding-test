"""
88. Merge Sorted Array
작성일: 2025년 9월 25일

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        # O((m+n) log(m+n)) time | O(m+n) space
        # Due to time sorting
        nums1[:] = sorted(nums1[:m]+ nums2[:n])
        """
        p1 = m - 1
        p2 = n - 1
        p  = m + n - 1

        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p  -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p  -= 1
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]


# Test case
s = Solution()

# Test case 1
nums1_1 = [1,2,3,0,0,0]
m1, nums2_1, n1 = 3, [2,5,6], 3
expected_1 = [1,2,2,3,5,6]
original_id_1 = id(nums1_1)
print(f"Before: nums1 = {nums1_1}, id = {original_id_1}")
s.merge(nums1_1, m1, nums2_1, n1)
print(f"After:  nums1 = {nums1_1}, id = {id(nums1_1)}")
print(f"Expected: {expected_1}")
print(f"Same object? {original_id_1 == id(nums1_1)}")  # Should be True for in-place
print(f"Correct result? {nums1_1 == expected_1}")
print()

# Test case 2
nums1_2 = [1]
m2, nums2_2, n2 = 1, [], 0
expected_2 = [1]
original_id_2 = id(nums1_2)
print(f"Before: nums1 = {nums1_2}, id = {original_id_2}")
s.merge(nums1_2, m2, nums2_2, n2)
print(f"After:  nums1 = {nums1_2}, id = {id(nums1_2)}")
print(f"Expected: {expected_2}")
print(f"Same object? {original_id_2 == id(nums1_2)}")  # Should be True for in-place
print(f"Correct result? {nums1_2 == expected_2}")
print()

# Test case 3
nums1_3 = [0]
m3, nums2_3, n3 = 0, [1], 1
expected_3 = [1]
original_id_3 = id(nums1_3)
print(f"Before: nums1 = {nums1_3}, id = {original_id_3}")
s.merge(nums1_3, m3, nums2_3, n3)
print(f"After:  nums1 = {nums1_3}, id = {id(nums1_3)}")
print(f"Expected: {expected_3}")
print(f"Same object? {original_id_3 == id(nums1_3)}")  # Should be True for in-place
print(f"Correct result? {nums1_3 == expected_3}")