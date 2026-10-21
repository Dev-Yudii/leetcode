"""
This problem was extracted on 2026-10-19 14:35 (UTC-3) from LeetCode at https://leetcode.com/problems/find-target-indices-after-sorting-array/.
You can check the full problem description there.
Problem Title:
    Find Target Indices After Sorting Array
Difficulty:
    Easy
Tags:
    Array, Binary Search, Sorting
"""

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [1,2,5,2,3], target = 2  |  Expected Output: [1,2]
    inputs1 = {}
    exec('nums = [1,2,5,2,3] ; target = 2', {}, inputs1)
    print(f'Test 1 Result:', solution.targetIndices(**inputs1), ' | Expected:', '[1,2]')

    # Example Input: nums = [1,2,5,2,3], target = 3  |  Expected Output: [3]
    inputs2 = {}
    exec('nums = [1,2,5,2,3] ; target = 3', {}, inputs2)
    print(f'Test 2 Result:', solution.targetIndices(**inputs2), ' | Expected:', '[3]')

    # Example Input: nums = [1,2,5,2,3], target = 5  |  Expected Output: [4]
    inputs3 = {}
    exec('nums = [1,2,5,2,3] ; target = 5', {}, inputs3)
    print(f'Test 3 Result:', solution.targetIndices(**inputs3), ' | Expected:', '[4]')

"""
Notes:
    -
"""
