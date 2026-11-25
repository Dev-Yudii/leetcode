"""
This problem was extracted on 2026-11-25 09:52 (UTC+0) from LeetCode at https://leetcode.com/problems/smallest-unique-subarray/.
You can check the full problem description there.
Problem Title:
    Smallest Unique Subarray
Difficulty:
    Hard
Tags:
    Array, Hash Table, Binary Search, Rolling Hash, Suffix Array, Hash Function
"""

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: nums = [3,3,3]  |  Expected Output: 3
    inputs1 = {'nums': [3, 3, 3]}
    print(f'Test 1 Result:', solution.smallestUniqueSubarray(**inputs1), ' | Expected:', 3)

    # Example Input: nums = [2,1,2,3,3]  |  Expected Output: 1
    inputs2 = {'nums': [2, 1, 2, 3, 3]}
    print(f'Test 2 Result:', solution.smallestUniqueSubarray(**inputs2), ' | Expected:', 1)

    # Example Input: nums = [1,1,2,2,1]  |  Expected Output: 2
    inputs3 = {'nums': [1, 1, 2, 2, 1]}
    print(f'Test 3 Result:', solution.smallestUniqueSubarray(**inputs3), ' | Expected:', 2)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
