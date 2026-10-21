"""
This problem was extracted on 2026-10-10 09:33 (UTC-3) from LeetCode at https://leetcode.com/problems/minimum-sum-of-squared-difference/.
You can check the full problem description there.
Problem Title:
    Minimum Sum of Squared Difference
Difficulty:
    Medium
Tags:
    Array, Binary Search, Greedy, Sorting, Heap (Priority Queue)
"""

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0  |  Expected Output: 579
    inputs1 = {}
    exec('nums1 = [1,2,3,4] ; nums2 = [2,10,20,19] ; k1 = 0 ; k2 = 0', {}, inputs1)
    print(f'Test 1 Result:', solution.minSumSquareDiff(**inputs1), ' | Expected:', '579')

    # Example Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1  |  Expected Output: 43
    inputs2 = {}
    exec('nums1 = [1,4,10,12] ; nums2 = [5,8,6,9] ; k1 = 1 ; k2 = 1', {}, inputs2)
    print(f'Test 2 Result:', solution.minSumSquareDiff(**inputs2), ' | Expected:', '43')

"""
Notes:
    -
"""
