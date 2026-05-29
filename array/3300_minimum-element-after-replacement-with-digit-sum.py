"""
Problem:
    Minimum Element After Replacement With Digit Sum
Link:
    https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
Difficulty:
    Easy
Topics:
    Array, Math
"""
from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        results = []

        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            results.append(digit_sum)

        return min(results)
                
if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [10,12,13,14]  |  Expected Output: 1
    testcase1 = [10,12,13,14]
    print(f'Test 1 Result:', solution.minElement(testcase1))

    # Example Input: nums = [1,2,3,4]  |  Expected Output: 1
    testcase2 = [1,2,3,4]
    print(f'Test 2 Result:', solution.minElement(testcase2))

    # Example Input: nums = [999,19,199]  |  Expected Output: 10
    testcase3 = [999,19,199]
    print(f'Test 3 Result:', solution.minElement(testcase3))


"""
Approach 1:
    - Convert integers into strings, iterate each turning digits into integers again to sum them
    - append the sum in a new list
    - return minimun value of the list 
Issue:
    - 
Final Approach:
    - Approach - passed on LeetCode with
        Runtime 7 ms Beats 30.84%
        Memory 19.27 MB Beats 56.38%

Complexity:
    Time: O(n * k)
    Space: O(n)
Notes:
    - 
"""
