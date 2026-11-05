"""
This problem was extracted on 2026-11-05 11:20 (UTC+0) from LeetCode at https://leetcode.com/problems/find-x-value-of-array-i/.
You can check the full problem description there.
Problem Title:
    Find X Value of Array I
Difficulty:
    Medium
Tags:
    Array, Math, Dynamic Programming
"""

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [1,2,3,4,5], k = 3  |  Expected Output: [9,2,4]
    inputs1 = {'nums': [1, 2, 3, 4, 5], 'k': 3}
    print(f'Test 1 Result:', solution.resultArray(**inputs1), ' | Expected:', [9, 2, 4])

    # Example Input: nums = [1,2,4,8,16,32], k = 4  |  Expected Output: [18,1,2,0]
    inputs2 = {'nums': [1, 2, 4, 8, 16, 32], 'k': 4}
    print(f'Test 2 Result:', solution.resultArray(**inputs2), ' | Expected:', [18, 1, 2, 0])

    # Example Input: nums = [1,1,2,1,1], k = 2  |  Expected Output: [9,6]
    inputs3 = {'nums': [1, 1, 2, 1, 1], 'k': 2}
    print(f'Test 3 Result:', solution.resultArray(**inputs3), ' | Expected:', [9, 6])

"""
Notes:
    -
"""
